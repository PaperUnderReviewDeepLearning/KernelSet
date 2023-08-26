__all__ = ['normal', 'resnet', 'resnet_block', 'vgg']

from models.accessor import get_model

from models.normal import NormalCNN
from models.resnet import Resnet
from models.resnet_block import ResnetBlock
from models.vgg import VGG