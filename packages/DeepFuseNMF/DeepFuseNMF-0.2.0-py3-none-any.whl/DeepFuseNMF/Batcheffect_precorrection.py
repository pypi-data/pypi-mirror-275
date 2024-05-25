##Use the normalized spot expression profile from all tissue
import numpy as np

nmf_input = np.vstack(spot_expression_profile_np_list)
tissue_label = np.hstack([np.repeat(Section_name_list[tissue_index],(spot_expression_profile_np_list[tissue_index].shape[0])) for tissue_index in range(len(spot_coord_list))])
##
model_NMF = skdecom.NMF(n_components=rank_use, init='nndsvd', random_state=None, max_iter=2000)
spot_region_score_init_tem_alltissue = model_NMF.fit_transform(nmf_input)
metagene_init_tem = model_NMF.components_
##Before normalized, remove the batch effect
Section_name_list = ["Palbocilib_A","Palbocilib_B","Control_C","Control_D"]
# reference tissue for Section_name_list
Section_name_reference_list = ["Palbocilib_A","Palbocilib_A","Control_C","Control_C"]
gamma_list = []
spot_region_score_init_tem_alltissue_copy = spot_region_score_init_tem_alltissue.copy()
for Section_name_cur in Section_name_list:
    tissue_index = np.where(np.array(Section_name_list) == Section_name_cur)[0]
    Section_name_reference_cur = Section_name_reference_list[tissue_index]
    ##Remove batch effect
    spot_region_score_curtissue = spot_region_score_init_tem_alltissue[tissue_label == Section_name_cur,:].copy()
    spot_region_score_reference = spot_region_score_init_tem_alltissue[tissue_label == Section_name_reference_cur,:].copy()
    ##Means embedding intensity (1 by Rank_use)
    spot_region_score_curtissue_mean = np.mean(spot_region_score_curtissue,axis = 0)
    spot_region_score_reference_mean = np.mean(spot_region_score_reference, axis=0)
    beta_cur = spot_region_score_curtissue_mean - spot_region_score_reference_mean
    ##gamma (1 by Gene_num)
    gamma_cur = np.matmul(np.resize(beta_cur,(1,spot_region_score_curtissue_mean.shape[1])),
                          metagene_init_tem)
    gamma_list.append(gamma_cur.copy())
    ##
    spot_region_score_curtissue = spot_region_score_curtissue - np.matmul(np.ones(shape=(spot_region_score_curtissue.shape[0], 1)), np.resize(beta_cur, (1, spot_region_score_curtissue.shape[1])))
    negative_index = np.where(spot_region_score_curtissue < 0)
    spot_region_score_curtissue[negative_index[0], negative_index[1]] = 0
    spot_region_score_init_tem_alltissue_copy[tissue_label == Section_name_cur,:] = spot_region_score_curtissue

##Normalization of NMF
# spot_region_score_init_tem_alltissue,metagene_init_tem = NMF_normalization_fun(spot_region_score_init_tem_alltissue = spot_region_score_init_tem_alltissue,
spot_region_score_init_tem_alltissue,metagene_init_tem = NMF_normalization_fun(spot_region_score_init_tem_alltissue = spot_region_score_init_tem_alltissue_copy,
                                                                                         metagene_init_tem = metagene_init_tem)
# spot_region_score_init_tem_alltissue
# metagene_init_tem
# gamma_list