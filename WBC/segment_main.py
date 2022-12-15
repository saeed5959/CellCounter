import cv2
import numpy as np
import os

from core.settings import WBC_Segment_Config

#parameter
THRESHOLD = WBC_Segment_Config.threshold
KERNEL = WBC_Segment_Config.kernel
BOUNDARY = WBC_Segment_Config.boundary

def segment(img_path:str):
    
    #loading image
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

    #threshold
    ret,img_thresh = cv2.threshold(img_gray,THRESHOLD,255,cv2.THRESH_BINARY)
    
    #kernel
    kernel = np.ones((KERNEL,KERNEL),np.uint8)
    img_erosion = cv2.erode(img_thresh,kernel,iterations=1)
    
    #connect component
    nb_comp,output,sizes,centroids = cv2.connectedComponentsWithStats(img_erosion,connectivity=4)

    #taking away the background
    nb_comp-=1; sizes=sizes[1:,-1]; centroids=centroids[1:,:]
    
    counter = 0
    #drawing X
    for label in range(0,np.size(sizes)):
        if sizes[label]>BOUNDARY:
            counter += 1
            cordinate = np.uint16(centroids[label])
            img_out = img[cordinate[1]-200:cordinate[1]+200,cordinate[0]-200:cordinate[0]+200]
            img_out_path = os.path.join(os.path.dirname(img_path),f"{counter}.jpg")
            cv2.imwrite(img_out_path,img_out)
            
    return counter, img_out_path