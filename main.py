import argparse

from RBC import rbc_main
from WBC import segment_main,classify_main


def rbc_count(img_path:str):
    
    rbc_nums, rbc_radius_mean, rbc_volume_mean, img_out_path = rbc_main(img_path)
    
    print(f"numbers of RBC = {rbc_nums}")
    print(f"radius mean of RBC = {rbc_radius_mean}")
    print(f"volume mean of RBC = {rbc_volume_mean}")
    print(f"output image path is : {img_out_path}")
    
    return

def wbc_classify_infer(img_path:str,model_path:str):
    
    output = classify_main.model_infer(img_path, model_path)
    
    if output==0:
        print("this image belongs to neutrophil group")
    
    elif output==1:
        print("this image belongs to basophil group")
        
    elif output==2:
        print("this image belongs to esophil group")
        
    elif output==3:
        print("this image belongs to lamphocyte group")
        
    else:
        print("this image belongs to monocyte group")
        
    return 

def wbc_classify_train(dataset_file:str ,model_path:str):
    
    classify_main.model_train(dataset_file ,model_path)
    
    

def wbc_segment(img_path):
    
    wbc_nums, img_out_path = segment_main(img_path)
    
    print(f"numbers of WBC = {wbc_nums}")
    print(f"output image path is : {img_out_path}")
    
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, required=True)
    parser.add_argument("--img_path", type=str, required=False)
    parser.add_argument("--dataset_file", type=str, required=False)
    parser.add_argument("--model_path", type=str, required=False)
    args = parser.parse_args()
    
    if args.mode == "rbc_count":
        rbc_count(args.img_path)
        
    elif args.mode == "wbc_classfiy_infer":
        wbc_classify_infer(args.img_path,args.model_path)
        
    elif args.mode == "wbc_classfiy_train":
        wbc_classify_train(args.dataset_file, args.model_path)
        
    elif args.mode == "wbc_segment":
        wbc_segment(args.img_path)
        
    else:
        print("please enter your --mode from these : rbc_count  , wbc_classify  , wbc_segment ")
                
