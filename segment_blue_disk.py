# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:37:10 2018

@author: Jeremy
"""

#Hough Transform method (circle detection);


import numpy as np
import cv2
import os



def segment_blue_disk(Image):

    IM=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY);
    
    
    Image=cv2.medianBlur(Image,5)
    
    circles = cv2.HoughCircles(IM,cv2.HOUGH_GRADIENT,dp=1,minDist=52,
                            param1=31,param2=70,minRadius=50,maxRadius=325)
    
    

    circles = np.uint16(np.around(circles))
    circles=circles[0]
    index=0
    
    for i in circles:
        
        if(i[2]==np.max(circles[:,2])):
            # draw the outer circle
            cv2.circle(IM,(i[0],i[1]),i[2],(255,255,0),2);
            # draw the center of the circle
            cv2.circle(IM,(i[0],i[1]),2,(0,0,255),3);
            
            xmin=i[0]-i[2];
            xmax=i[0]+i[2];
            ymin=i[1]-i[2];
            ymax=i[1]+i[2];
            
            bbox=np.array([[ymin,ymax,xmin,xmax]]);
        
            cv2.imshow('detected circles',IM);
            cv2.waitKey(0);
            cv2.destroyAllWindows();
        
            return bbox;
        
        index=index+1;

    
    return circles;
    
def main():
    
    
    os.chdir("C:\\Users\\Jeremy");
    filename="C:\\Users\\Jeremy\\disk0\\_0.png";
    
    return(segment_blue_disk(cv2.imread(filename)))
    
