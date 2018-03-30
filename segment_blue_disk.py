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

def segment_blue_disk(Image,boolean=False,return_bbox=False):
    
    if(boolean):
        
        
        
        start_time=time.time();
        
    IM=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY);
    #IM=cv2.GaussianBlur(IM,(3,3),5)
    #IM=cv2.medianBlur(IM,3)
    IM=cv2.Canny(IM,15,60,L2gradient=True)
    
        

    circles = cv2.HoughCircles(IM,cv2.HOUGH_GRADIENT,dp=1.0,minDist=55,
                            param1=40,param2=150,minRadius=0,maxRadius=0)
    
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
                
                    cv2.imshow('detected circles',Image);
                    cv2.imshow('processed image',IM);
                    end_time=time.time();
                    print(str(float(end_time-start_time))+" seconds to run ")
                    cv2.waitKey(0);
                    cv2.destroyAllWindows();
                    
                if(return_bbox):
                    
                    
                    return bbox;
                
                else:
                    
                    
                    return Image[ymin:ymax,xmin:xmax,:];
        
    else:
        
        if(return_bbox):
        
            return [0,IM.shape[0],0,IM.shape[1]];
        
        else:
            
            return Image;
    
def main_test(number=0):
    
    os.chdir("C:/Users/Jeremy/");
    pathname="C:\\Users\\Jeremy\\disk"+str(number)+"\\_0.png";
    Image=cv2.imread(pathname);
    segment_blue_disk(Image,boolean=True)


    