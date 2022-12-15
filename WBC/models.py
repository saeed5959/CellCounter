import torch
from torch import nn
import torch.nn.functional as F


class model_cnn(nn.Module):
    def __init__(self,config:object):
        super().__init__()
        
        self.kernel_size = config.kernel_size
        self.in_channels = config.n_channels
        self.filtes = config.filters
        self.linear_dim = config.lenear_dim
        self.n_category = config.n_category
        
        self.cnn_block = nn.ModuleList(
            nn.Conv2d(self.in_channels,self.filtes[0],self.kernel_size),
            nn.MaxPool2d(self.kernel_size),
        
            nn.Conv2d(self.filtes[0],self.filtes[1],self.kernel_size),
            nn.MaxPool2d(self.kernel_size),
        
            nn.Conv2d(self.filtes[1],self.filtes[2],self.kernel_size,),
            nn.MaxPool2d(self.kernel_size))
        
        self.linear_block = nn.ModuleList(
            nn.Linear(1,self.linear_dim),
            nn.Linear(self.linear_dim,self.n_category))
        
    def forward(self,img):
        img_cnn = self.cnn_block(img)
        out_linear = self.linear_block(img_cnn)
        
        output = F.sigmoid(out_linear)
        return output
    
