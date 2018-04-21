# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:02:13 2018

@author: Jeremy
"""


import numpy as np
from operator import itemgetter
import cv2
import os
import copy
from processing_libs import get_data,normalize #processing_libs functions


def get_angle_value(current_image,image_vector):

    
    my_vector=[];
    
    for image in image_vector:
        
        
        my_vector.append(np.abs(np.mean(current_image-image)))
        
        
    return min(enumerate(my_vector), key=itemgetter(1))[0] 
        
        

filename="training_data.pkl";   #file name of pickle file of training_data
os.chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");  #change python 
data=get_data(filename);
im=np.array(data[1]);                                         #training image data
im=normalize(im) 
del data
cap=cv2.VideoCapture(1);
ret,frame=cap.read();
new_IM=copy.deepcopy(frame);
new_IM=normalize(new_IM);
angle=get_angle_value(new_IM,im
                      )
cv2.imshow('frame',frame);
cv2.waitKey(0);

    
    
    
    