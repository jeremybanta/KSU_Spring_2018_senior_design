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
import os;
os.chdir("C:/Users/Jeremy/Desktop/Senior Project Design")

import numpy as np
from operator import itemgetter
import pickle
import cv2
import time;
from segment_blue_disk import segment_blue_disk
import os
from template_matching import get_blue_disk_angle;

cap=cv2.VideoCapture(1);




training_type=input('enter what type you want to test performance on? ')

def Main():
    
    while(True):
        
        input();
        
        ret,frame=cap.read();
        
        if(ret):
            
            frame=segment_blue_disk(frame)
            theta=get_blue_disk_angle(frame)
            cv2.imshow('frame',frame);
            cv2.waitKey()
            
            if(theta<0):
                
                theta=theta+360;
                
            print(theta);
            
    cap.release();
    cv2.destroyAllWindows();
            
if(training_type=='matching'):
    
    Main();
    
if(training_type=='cnn'):
    
    from keras.models import load_model
    from processing_libs import getAngle,normalize

    model=load_model("model.h5");
    model2=load_model("model_final.h5")
    model3=load_model("model_deep_learning.h5")

    
    while True:
        
        
        ret,frame=cap.read();

        
        if(ret):
            
            start_time=time.time()
            frame=segment_blue_disk(frame);
            frame=cv2.resize(frame,(215,215))
            cv2.imshow('frame',frame)
            cv2.waitKey()
            #frame=cv2.medianBlur(frame,5)
            frame=normalize(frame);
            cos_sin_vector=model.predict(np.reshape(frame,(1,215,215,3)));
            cos_sin_vector2=model2.predict(np.reshape(frame,(1,215,215,3)));
            cos_sin_vector3=model3.predict(np.reshape(frame,(1,215,215,3)));
            angle=getAngle(cos_sin_vector);
            angle2=getAngle(cos_sin_vector2)
            angle3=getAngle(cos_sin_vector3)
            angle=np.mod(np.mean([angle,angle2,angle3]),120)
            
            print(angle);
            
            end_time=time.time();
            print("elapsted time is: "+str(float(end_time-start_time))+" in seconds");
            
        
            
    cap.release();
    cv2.destroyAllWindows();