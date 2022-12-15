import torch
from torch import nn
from torch.utils.data import DataLoader
import cv2

from data_utils import DatasetImg
from models import model_cnn
from core.configs import WbcClassifyConfig

#parameters
epochs = WbcClassifyConfig.epochs
batch_size = WbcClassifyConfig.batch_size
lr = WbcClassifyConfig.lr


def model_train(dataset_file:str ,model_path:str):
    
    dataset_class = DatasetImg(dataset_file)
    dataloader = DataLoader(dataset_class, batch_size=batch_size, shuffle=True) 
    
    model = model_cnn(WbcClassifyConfig)
    loss = nn.NLLLoss()
    optimizer = torch.optim.SGD(model.parameters(),lr=lr)
    
    
    for epoch in range(1,epochs):
        print("epoch "+str(epoch)+"**")
        
        for num, (img, n_class) in enumerate(dataloader):
            out = model(img)
            loss_out = loss(out, n_class)

            optimizer.zero_grad()
            loss_out.backward()
            optimizer.step()

            print("loss : " + str(loss_out.item()))
            
    
    torch.save({'model': model.state_dict(),
                'iteration': epochs}, model_path)
            
    return


def model_infer(img_path:str,model_path:str):
    
    model = model_cnn(WbcClassifyConfig)
    model_pretrain = torch.load(model_path, map_location='cpu')
    model.state_dict = model_pretrain["model"]
    
    img = cv2.imread(img_path) / 255
    img_tensor = torch.Tensor(img)
    
    output = model(img_tensor)
    
    return output