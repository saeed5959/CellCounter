import torch
import cv2
from torch.utils.data import Dataset


class DatasetImg(Dataset):
    def __init__(self,img_path_text:str):
        super().__init__()
        with open(img_path_text) as file:
            img_path_class_file = file.readlines()
        
        self.img_path_class = []
        for line in img_path_class_file:
            img_path, img_class = line.split("|")
            self.img_path_class.append([img_path,img_class])
            
    def get_img_class(self,data:list):
        img_path, img_class = data[0], data[1]
        img = cv2.imread(img_path) / 255
        img_tensor = torch.Tensor(img)
        
        return img_tensor, img_class 
        
    def __getitem__(self,index):
        return self.get_img_class(self.img_path_class[index])
    
    def __len__(self):
        return len(self.img_path_class)