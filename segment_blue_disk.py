# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:37:10 2018
@author: Jeremy
"""

#Hough Transform method (circle detection);

import numpy as np
import cv2
import time
import os
from scipy.ndimage.morphology import binary_fill_holes


def segment_blue_disk(Image,boolean=False,return_bbox=False,number=None):
    
    start_time=time.time();

    IM=cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)[:,:,0];
    IM = cv2.medianBlur(IM,9);
    IM=cv2.Canny(IM,15,75);

    
    
    if(boolean):
        
        cv2.imshow('IM',IM);
        cv2.waitKey(0);
    
    
       
    
    circles = cv2.HoughCircles(IM,cv2.HOUGH_GRADIENT,dp=1.5,minDist=1,param1=100);
    
    if circles is not None:
        

        circles = np.uint16(np.around(circles));
        circles=circles[0];
    
        for i in circles:
        
            if(i[2]==np.max(circles[:,2])):
                
                i=np.int32(i)
            
                if(boolean):
                    # draw the outer circle
                    #if desired so
                    cv2.circle(Image,(i[0],i[1]),i[2],(255,255,0),2);
                    # draw the center of the circle
                    cv2.circle(Image,(i[0],i[1]),2,(0,0,255),3);
                
                xmax=i[0]+i[2];
                ymax=i[1]+i[2];
                
                if(i[1]-i[2]<0):
                    
                    ymin=0;
                    
                else:
                    
                    ymin=i[1]-i[2];
                    
                if(i[0]-i[2]<0):
                    
                    xmin=0;
                    
                else:
                    
                    xmin=i[0]-i[2];
            
                bbox=np.array([[ymin,ymax,xmin,xmax]],dtype=np.int32);
            
                if(boolean):

                    cv2.imshow('segmented image',IM);
                    cv2.imshow('detected circle',Image);
                    cv2.imshow('cropped image',Image[ymin:ymax,xmin:xmax,:]);
                    cv2.waitKey(0);
                    end_time=time.time();
                    print(str(float(end_time-start_time))+" seconds to run ");
                    
                    return(Image[ymin:ymax,xmin:xmax,:].shape)
                    
                if(return_bbox):
                    
                    
                    return bbox;
                
                else:
                    
                    
                    return Image[ymin:ymax,xmin:xmax,:];
        
    else:
        
        if(boolean):
            
            print("circles is None");
            
            return(Image.shape)
        
        elif(return_bbox):
        
            return [0,IM.shape[0],0,IM.shape[1]];
        
        else:
            
            return Image;
    
def main_test(number=0):
    
    os.chdir("C:/Users/Jeremy/");
    pathname="C:\\Users\\Jeremy\\disk"+str(number)+"\\_0.png";
    Image=cv2.imread(pathname);
    return segment_blue_disk(Image,boolean=True)