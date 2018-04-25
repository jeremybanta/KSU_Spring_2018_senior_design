# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:25:13 2018

@author: Jeremy
"""
import cv2
import time
import numpy as np
import os
from matplotlib import pyplot as plt
import pickle

os.chdir('C:\\Users\\Jeremy\Desktop\\Senior Project Design');

from segment_blue_disk import segment_blue_disk


def get_blue_disk_angle(img,plot_graphs=True):
    
    
    img=segment_blue_disk(img);
    img=cv2.resize(img,(215,215))
    template = cv2.imread('template.png')
    _,w, h = template.shape[::-1]
    inital_image=pickle.load(open("training_data.pkl","rb"))[1][0];
    

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        
        method = eval(meth);

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method);
        res_inital=cv2.matchTemplate(inital_image,template,method);
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res);
        min_val_inital,max_val_inital,min_loc_inital, max_loc_inital=cv2.minMaxLoc(res_inital);

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
            top_left_inital=min_loc_inital
        else:
            top_left = max_loc
            top_left_inital=max_loc_inital
            
            
        bottom_right = (top_left[0] + w, top_left[1] + h)
        bottom_right_inital=(top_left_inital[0]+2,top_left[1]+h)
        
        if plot_graphs:
            
            cv2.rectangle(img,top_left, bottom_right, 255, 2)
            plt.subplot(121),plt.imshow(res,cmap = 'gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(img,cmap = 'gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()
    
    
    
    angle1=np.arctan2((top_left[1]+bottom_right[1])/2,(top_left[0]+bottom_right[0])/2) #predicted angle
    angle2=np.arctan2((top_left_inital[1]+bottom_right_inital[1])/2,(top_left_inital[0]+
                      bottom_right_inital[0])/2)
    
    
    return np.mod((np.degrees(angle1-angle2)),360)
    
    
    