import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights


class DeepFuseNMFUnet(nn.Module):
    """
    Attribute:
        The `DeepFuseNMFUnet` model is a deep learning architecture for image and spot expression prediction.
        It integrates Non-negative Matrix Factorization (NMF) and low-rank representation, enabling efficient
        prediction and high-resolution pixel-wise embedding output.

    Args:
        rank (int): The rank of the low-rank representation.
        num_genes (int): The number of genes in the dataset.
        num_channels (int): The number of channels in the input image.

    Outputs of the model:
        image_pred (torch.Tensor): The predicted image.
        spot_exp_pred (torch.Tensor): The predicted spot expression.
        HR_score (torch.Tensor): The high-resolution pixel-wise embedding output.

    Example:
        >>> model = DeepFuseNMFUnet(rank=20, num_genes=1000, num_channels=3)
        >>> image = torch.rand(1, 3, 256, 256)
        >>> feasible_coord = {}
        >>> vd_score = torch.rand(1)
        >>> model(image, feasible_coord, vd_score)
    """
    def __init__(self,
                 rank: int = 20,
                 num_genes: int = 2000,
                 num_channels: int = 3,
                 section_names: list = None,
                 reference: list = None):
        """
            Initialize the `DeepFuseNMFUnet` model.
        """

        super(DeepFuseNMFUnet, self).__init__()
        self.num_genes = num_genes
        self.rank = rank
        self.num_channels = num_channels

        # Initial convolution block
        self.initial = nn.Sequential(
            nn.Conv2d(self.num_channels, 64, kernel_size=7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )

        # Up-sampling layers
        self.upsample_2x = nn.Sequential(
            nn.ConvTranspose2d(1024, 256, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        self.upsample_4x = nn.Sequential(
            nn.ConvTranspose2d(256, 128, kernel_size=4, stride=4),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )

        # Convolutional layers for feature fusion and transformation
        self.feature_fusion = nn.Sequential(
            nn.Conv2d(512, 256, kernel_size=3, padding=1, padding_mode="replicate"),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )

        # final output for prediction
        self.output = nn.Sequential(
            nn.Conv2d(128, self.num_channels, kernel_size=1, padding_mode='reflect'),
            nn.BatchNorm2d(self.num_channels),
            nn.Sigmoid()
        )

        # Low-rank representation block
        self.low_rank = nn.Sequential(
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=2, dilation=2, padding_mode='reflect'),
            nn.BatchNorm2d(128),
            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=2, dilation=2, padding_mode='reflect'),
            nn.BatchNorm2d(64),
            nn.ReLU(),

            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),

            nn.ConvTranspose2d(32, self.rank, kernel_size=4, stride=2, padding=1)
        )

        # self.low_rank = nn.Sequential(
        #     nn.Conv2d(128, 64, kernel_size=3, padding=1, padding_mode="replicate"),
        #     nn.BatchNorm2d(64),
        #     nn.LeakyReLU(negative_slope=0.2, inplace=True),
        #
        #     nn.Conv2d(64, self.rank, kernel_size=3, padding=1),
        # )

        # Image prediction block
        self.image_pred = nn.Sequential(
            nn.Conv2d(self.rank, 128, kernel_size=5, padding=2, padding_mode='reflect'),
            nn.ReLU(),

            nn.Conv2d(128, self.num_channels, kernel_size=1, padding_mode='reflect'),
            nn.BatchNorm2d(self.num_channels),
            nn.Sigmoid()
        )

        # Decoder for Non-negative Matrix Factorization (NMF)
        self.nmf_decoder = nn.Parameter(torch.randn(self.num_genes, self.rank), requires_grad=True)

        self.apply(__initial_weights__)
        self.training_mode = False

        # Load pre-trained FCN ResNet50 as the backbone
        self.backbone = fcn_resnet50(weights=FCN_ResNet50_Weights.DEFAULT, progress=False).backbone

        # Remove batch effect
        self.gamma = None
        if reference is not None:
            # gamma = torch.randn(len(reference), self.num_genes) * 1e-4
            gamma = torch.zeros(len(reference), self.num_genes)
            self.gamma = nn.Parameter(gamma, requires_grad=True)
            self.batch2idx = {section_names[idx]: torch.tensor(idx) for idx, name in enumerate(reference) if name is not None}

    def forward(self, image, section_name=None, feasible_coord=None, vd_score=None, encode_only=False):
        # Initial processing block
        x = self.initial(image)

        # Backbone layers
        x_ = self.backbone.layer1(x)
        x = self.backbone.layer2(x_)
        x = self.backbone.layer3(x)

        # Up-sampling and feature fusion
        x = self.upsample_2x(x)
        x = torch.cat((x, x_), dim=1)
        x = self.feature_fusion(x)
        x = self.upsample_4x(x)

        # for pretraining stage, only return the predicted image and patch features
        if not self.training_mode:
            image_pred = self.output(x)
            return image_pred, x

        # Low-rank representation
        low_rank_score = self.low_rank(x)
        vd_score_logit = torch.logit(vd_score, eps=1.388794e-11)
        HR_score = torch.sigmoid(vd_score_logit + low_rank_score)

        # Return high-resolution pixel-wise embedding output if only performing encoding
        if encode_only: return HR_score

        # Image prediction
        image_pred = self.image_pred(HR_score)

        # If no feasible coordinates are provided, return the image prediction and high-resolution pixel-wise embedding
        if len(feasible_coord) == 0: return image_pred, None, HR_score

        # Get spot scores through averaging the high-resolution pixel-wise embedding output
        spot_score = [torch.mean(HR_score[0, :, coord[0], coord[1]], dim=1) for _, coord in feasible_coord.items()]
        spot_score = torch.stack(spot_score, dim=0)

        # Predict spot expression based on multiplying the spot scores with the NMF decoder (all are non-negative)
        nmf_decoder_limited = torch.relu(self.nmf_decoder)
        spot_exp_pred = F.linear(spot_score, nmf_decoder_limited)

        # Remove batch effect
        if self.gamma is not None and section_name in self.batch2idx:
            batch_idx = self.batch2idx[section_name]
            spot_exp_pred = torch.relu(spot_exp_pred + self.gamma[batch_idx, :])

        return image_pred, spot_exp_pred, HR_score

class GraphConv(nn.Module):
    """
    Attribute:
        The `GraphConv` model is a graph convolutional layer for graph neural networks.

    Args:
        input_dim (int): The input dimension of the graph convolutional layer.
        output_dim (int): The output dimension of the graph convolutional layer.

    Output of the model:
        (torch.Tensor): The output tensor of the graph convolutional layer.
    """
    def __init__(self, input_dim: int, output_dim: int):
        """
        Attribute:
            Initialize the `GraphConv` model.
        """

        super(GraphConv, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x, adj):
        x = self.linear(x)
        return torch.mm(adj, x)


class GraphAutoEncoder(nn.Module):
    """
    Attribute:
        The `GraphAutoEncoder` model is a graph autoencoder for predicting spot embeddings.

    Args:
        adj_matrix (torch.Tensor): The adjacency matrix of the graph.
        rank (int): The rank of the graph autoencoder.
        num_spots (int): The number of spots in the dataset.

    Output of the model:
        y (torch.Tensor): Reconstructed spot embedding.

    Example:
        >>> adj_matrix = torch.rand(10, 10)
        >>> model = GraphAutoEncoder(adj_matrix, num_spots=5, rank=20)
        >>> score = torch.rand(5, 20)
        >>> model(score)
    """
    def __init__(self,
                 adj_matrix: torch.Tensor,
                 num_spots: int,
                 rank: int = 20):
        """
        Attribute:
            Initialize the `GraphAutoEncoder` model.
        """

        super(GraphAutoEncoder, self).__init__()
        self.rank = rank
        self.adj_matrix = adj_matrix

        # Parameters of pseudo spots' initial embeddings
        self.pseudo_score = nn.Parameter(torch.randn((adj_matrix.shape[0] - num_spots, rank)), requires_grad=True)

        # Define graph convolutional layers
        self.gc1 = GraphConv(input_dim=rank, output_dim=64)
        self.gc2 = GraphConv(input_dim=64, output_dim=256)
        self.gc3 = GraphConv(input_dim=256, output_dim=64)
        self.gc4 = GraphConv(input_dim=64, output_dim=rank)

        self.apply(__initial_weights__)

    def forward(self, score):
        # Apply sigmoid to latent strengths to limit their values
        pseudo_score = torch.sigmoid(self.pseudo_score)

        # Concatenate the real and pseudo spot embeddings
        x = torch.cat([score, pseudo_score], dim=0)

        # Graph Convolutional Layers
        x = F.relu(self.gc1(x, self.adj_matrix))
        x = F.relu(self.gc2(x, self.adj_matrix))
        x = F.relu(self.gc3(x, self.adj_matrix))

        # Reconstructed spot embedding whose values are limited to [0, 1]
        y = F.sigmoid(self.gc4(x, self.adj_matrix))

        return y


def __initial_weights__(module):
    # Initialize the weights of the model

    if isinstance(module, nn.Conv2d):
        init.kaiming_normal_(module.weight, mode='fan_out', nonlinearity='relu')
        if module.bias is not None:
            init.constant_(module.bias, 0)
    elif isinstance(module, nn.BatchNorm2d):
        init.constant_(module.weight, 1)
        init.constant_(module.bias, 0)
    elif isinstance(module, nn.Linear):
        init.kaiming_normal_(module.weight, mode='fan_out', nonlinearity='relu')
        if module.bias is not None:
            init.constant_(module.bias, 0)
