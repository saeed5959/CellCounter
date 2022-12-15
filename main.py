import argparse

from RBC import rbc_main
from WBC import segment_main


def rbc_count(img_path):
    
    rbc_nums, rbc_radius_mean, rbc_volume_mean, img_out_path = rbc_main(img_path)
    
    print(f"numbers of RBC = {rbc_nums}")
    print(f"radius mean of RBC = {rbc_radius_mean}")
    print(f"volume mean of RBC = {rbc_volume_mean}")
    print(f"output image path is : {img_out_path}")
    
    return

def wbc_classify(img_path):
    
    return

def wbc_segment(img_path):
    
    wbc_nums, img_out_path = segment_main(img_path)
    
    print(f"numbers of WBC = {wbc_nums}")
    print(f"output image path is : {img_out_path}")
    
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, required=True)
    parser.add_argument("--img_path", type=str, required=True)
    args = parser.parse_args()
    
    if args.mode == "rbc_count":
        rbc_count(args.img_path)
        
    elif args.mode == "wbc_classiy":
        wbc_classify(args.img_path)
        
    elif args.mode == "wbc_segment":
        wbc_segment(args.img_path)
        
    else:
        print("please enter your --mode from these : rbc_count  , wbc_classify  , wbc_segment ")
                
