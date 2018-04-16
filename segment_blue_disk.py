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


def segment_blue_disk(Image,boolean=False,return_bbox=False,number=None):
    
    start_time=time.time();                          #time object name start_time

    IM=cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)[:,:,0];   #convert RGB to HSV colorspace only get Hue
    #which corresponds to the true color of a particular image
    IM = cv2.medianBlur(IM,9);                         #compute medianblur with (9,9) kernel size
    IM=cv2.Canny(IM,15,75);                            

    
    
    if(boolean):                        #optional flag for displaying image
        
        cv2.imshow('IM',IM);             #display image
        cv2.waitKey(0);                  #delay 0ms
    
    
       
    
    circles = cv2.HoughCircles(IM,cv2.HOUGH_GRADIENT,dp=1.5,minDist=1,param1=100);
    #houghcircl transform to find circles in image
    #this is used primarly to find the roi of where the bluedisk is in the image
    #and then cut out areas outside this region this will be able to make the
    #system more robust
    
    if circles is not None: #if there are circles found with the HoughCircles transform then 
        

        circles = np.uint16(np.around(circles));
        #round the values of circles
        circles=circles[0];
        #get back circles from tuple of list of lists
    
        for i in circles:
            
            #for each elements in circles do the following
        
            if(i[2]==np.max(circles[:,2])):
                
                #if the second element of i is equal to max possible value of i[2]
                
                i=np.int32(i)  #convert i to int32
            
                if(boolean):  #if boolean flag is true draw the circles
                    # draw the outer circle
                    #if desired so
                    cv2.circle(Image,(i[0],i[1]),i[2],(255,255,0),2);
                    # draw the center of the circle
                    cv2.circle(Image,(i[0],i[1]),2,(0,0,255),3);
                
                xmax=i[0]+i[2];            #xmax value
                ymax=i[1]+i[2];            #ymax value
                
                if(i[1]-i[2]<0):           #if miny outside the screen window
                    
                    ymin=0;                #then set ymin equal to zero
                    
                else:
                    
                    ymin=i[1]-i[2];      #if miny inside screen then get actuall value of miny
                    
                if(i[0]-i[2]<0):          #if minx outside screen
                    
                    xmin=0;               #then set xmin equal to zero
                    
                else:
                    
                    xmin=i[0]-i[2];      #if xmin inside screen then get actuall value of minx
            
                bbox=np.array([[ymin,ymax,xmin,xmax]],dtype=np.int32); #bounding box of circle found
            
                if(boolean):               #if flage is true

                    cv2.imshow('segmented image',IM); #plot images for testing purposes
                    cv2.imshow('detected circle',Image);
                    cv2.imshow('cropped image',Image[ymin:ymax,xmin:xmax,:]);
                    cv2.waitKey(0);
                    end_time=time.time();
                    print(str(float(end_time-start_time))+" seconds to run ");
                    
                    return(Image[ymin:ymax,xmin:xmax,:].shape)
                    
                if(return_bbox):     #if return bbox flag is true
                    
                    
                    return bbox;     #return bbox
                
                else:  #else #return the image cropped ymin:ymax,xmin:xmax
                    
                    
                    return Image[ymin:ymax,xmin:xmax,:];
        
    else:
        
        if(boolean):    #if flag is true
            
            print("circles is None"); #print testing/ debugging information to the screen
            
            return(Image.shape)    #return the shape of the image
        
        elif(return_bbox):  #return bounding box flag true
        
            return [0,IM.shape[0],0,IM.shape[1]];  #return bbox of entire image
        
        else:
            
            return Image;   #return entire image
    
def main_test(number=0):    #test function
    
    os.chdir("C:/Users/Jeremy/");
    pathname="C:\\Users\\Jeremy\\disk"+str(number)+"\\_0.png";
    Image=cv2.imread(pathname);
    return segment_blue_disk(Image,boolean=True)   #segment blue disk with debug/test bit true