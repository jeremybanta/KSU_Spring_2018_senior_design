# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:32:23 2018

@author: Jeremy
"""


'''
Define boolean variables to be True iff 
the user wants to add the implementation of these algorithms to the
Computer Vision System

'''


import numpy as np
import pickle
import cv2
import os

os.chdir("C:/Users/Jeremy/Disktop/Senior Project Design")

from template_matching import get_blue_disk_angle;

cap=cv2.VideoCapture(1);


def Main():
    
    while(True):
        
        input();
        
        ret,frame=cap.read();
        
        if(ret):
            
            theta=get_blue_disk_angle(frame)
            
            cv2.imshow('frame',frame);
            cv2.waitKey()
            
            if(theta<0):
                
                theta=theta+360;
                
            print(theta);
            
    
        
        
        
        
        
        
        
        
    
