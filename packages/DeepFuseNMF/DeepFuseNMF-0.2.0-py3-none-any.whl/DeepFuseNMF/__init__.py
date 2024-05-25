r'''
DeepFuseNMF
'''

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from pkg_resources import get_distribution
    version = lambda name: get_distribution(name).version

from .train import DeepFuseNMF_Runner
from .data import spatial_obj
from .utils import visualize_score

name = "DeepFuseNMF"
__version__ = version(name)
__author__ = "Junjie Tang, Kun Qian"
