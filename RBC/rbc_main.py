import numpy as np
import cv2
import imutils
import os

from core.settings import RBC_CONFIG 

#parameter
THRESHOLD = RBC_CONFIG.threshold
BOUNDARY_LOW = RBC_CONFIG.boundary_low
BOUNDARY_UP = RBC_CONFIG.boundary_up


def counter(img_path:str):

    #reading image
    img = cv2.imread(img_path)

    #converting to grayscale
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img_copy = np.copy(img)

    #local histogram equalizer
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_equalize = clahe.apply(img_gray)

    #threshold
    ret,img_thresh = cv2.threshold(img_equalize,THRESHOLD,255,cv2.THRESH_BINARY)

    # noise removal
    kernel = np.ones((3,3),np.uint8)

    back_ground_sure = cv2.dilate(img_thresh,kernel,iterations=3)

    img_unknown = cv2.subtract(back_ground_sure,img_thresh)

    # Marker labelling
    ret, markers = cv2.connectedComponents(img_thresh)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[img_unknown==255] = 0

    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]

    labels = markers
    radius = np.zeros(np.max(labels)+1)
    i = 0

    for label in np.unique(labels):
        # if the label is zero, it is background so simply ignore it
        if label == 0:
            continue
        
        # otherwise, draw it on the mask
        mask = np.zeros(img_gray.shape, dtype="uint8")
        mask[labels == label] = 255
        
        # detect contours in the mask and grab the largest one
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnt = max(cnts, key=cv2.contourArea)
        
        # draw a circle enclosing the object
        ((x, y), radius[i]) = cv2.minEnclosingCircle(cnt)

        if (radius[i]>BOUNDARY_LOW)&(radius[i]<BOUNDARY_UP):
            cv2.circle(img_copy, (int(x), int(y)), int(radius[i]), (255,0, 0), 2)
            i +=1
            
    radius = radius[radius!=0]
    rbc_nums,rbc_radius_mean,rbc_volume_mean = rbc_meter(radius)
    
    img_out_path = os.path.join(os.path.basename(img_path)+"img_out.jpg")
    cv2.imwrite(img_out_path,img_copy)
    
    return rbc_nums, rbc_radius_mean, rbc_volume_mean, img_out_path



def rbc_meter(radius):
    #numbers of rbc
    rbc_nums = np.size(radius)
    
    #radius of rbc by multiplying 0.186 to convert to meter
    rbc_radius = radius*0.186
    rbc_radius_mean = np.mean(rbc_radius)
    
    #volume of rbc 
    rbc_volume = (4/3)*np.pi*(rbc_radius)**3
    rbc_volume_mean = np.mean(rbc_volume)
    
    return rbc_nums,rbc_radius_mean,rbc_volume_mean


