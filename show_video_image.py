# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 23:12:39 2018

@author: Jeremy
"""


for name in dir():
    if not name.startswith('_'):
        del globals()[name]
        
        
import cv2                     #import OpenCV
import numpy as np             #import numpy


cap=cv2.VideoCapture(1)                                  #make VideoCapture object of USB webcam
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5);    #width of image
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5);  #height of image


while(True):                                 #while true
    ret,frame=cap.read();                    #read image from webcam
    dst=frame;                               #set dst to frame of webcam
    cv2.imshow('frame',dst);                 #display image video in realtime
    cv2.waitKey(10);                         #wait 10ms before update
    if(cv2.waitKey(1) & 0xFF == ord('q')):   
        break;                               #break out of while loop
        
        
cap.release();                             #release cap
cv2.destroyAllWindows();                   #destroyAllWindows