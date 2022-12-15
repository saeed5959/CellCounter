import torch


class DatasetImg(torch.utils.data.Dataset):
    def __init__(self,img_path_text) -> None:
        super().__init__()
        with open(img_path_text) as file;
            self.img_text = file.read()
            
        
    def __getitem__(self,index):
        return self.get_img_class(self.img_text[index])