# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:13:39 2018
@author: Jeremy
"""

import cv2
import numpy as np
import segment_blue_disk
from keras.models import load_model
import os
import time
import gc;
import copy;
from processing_libs import getAngle,resize,normalize



os.chdir("C:\\Users\\Jeremy\\Desktop\\Senior Project Design");
model=load_model("model.h5");




def get_angle_degree_val(num,cap,plotting=True):   #gets the angle in degrees input argument is current test number
    #as an interger
    
    # Capture frame-by-frame
    
    
        
    cv2.waitKey(0)
    ret, frame = cap.read();  #ret true if image is retrived from camera false otherwise
    #frame is the image retrived from the camera
    IMAGE=copy.deepcopy(frame);
    #cv2.imwrite("C:\\Users\\Jeremy\\Desktop\\test_run_images\\t"+str(num)+".png",IMAGE)
    #get a deep copy of fram and assign it to the variable name of IMAGE
    start=time.time();
    #set time object to variable name of start
    IM=segment_blue_disk.segment_blue_disk(frame)
    #set IM to segment blue disk of the current frame
    IM=resize(IM);       #resize the image to size of (227,240)
    IM=normalize(IM)     #normalize the resized image
    pred=model.predict(IM);     #predict the outputs of the image sin(theta),cos(theta) values
    angle=getAngle(pred);        #predict angle value of image in degrees
    
    if(plotting):
    
        cv2.imshow('IMAGE',IMAGE);
        
        
        
    cv2.imwrite("C:\\Users\\Jeremy\\Desktop\\test_run_images\\t"+str(num)+str(angle)+".png",IMAGE)
    print(angle);
    #display angle value to the screen
    end=time.time();
    print(str(float(end-start))+" time in seconds for program to run one disk check ")
    #display the execution time of program to the screen
    cap.release()
    cv2.destroyAllWindows()
    gc.collect();
    
    cv2.destroyAllWindows()
    cap.release();
        
    return angle   #return angle value in degrees