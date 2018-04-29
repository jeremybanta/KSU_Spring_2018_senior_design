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
import gc
import time;
from segment_blue_disk import segment_blue_disk
import os
import RPi.GPIO as GPIO
from rpi_io import define_inputs_and_outputs, get_output,digitize_output,turn_off_all_ouput_io_pins
from template_matching import get_blue_disk_angle;

cap=cv2.VideoCapture(0);
training_type="cnn"

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
    
    
define_inputs_and_outputs();
    
if(training_type=='cnn'):
    
    from keras.models import load_model
    from processing_libs import getAngle,normalize

    model=load_model("model_experemntial.h5");

    while True:
        
        input()
        
        ret,frame=cap.read();

        
        if(ret):
            
            start_time=time.time()
            
            try:
                
                frame=segment_blue_disk(frame);
                frame=cv2.resize(frame,(215,215))
            
            except:
                
                while True:
                    
                    try:
                        
                        print("in the loop now in try except block")
                        
                        frame=segment_blue_disk(frame);
                        frame=cv2.resize(frame,(215,215))
                        break;
                        
                    except:
                        
                        continue
                        
            cv2.imshow('frame',frame)
            cv2.waitKey(1)
            #frame=cv2.medianBlur(frame,5)
            frame=normalize(frame);
            cos_sin_vector=model.predict(np.reshape(frame,(1,215,215,3)));
            angle=getAngle(cos_sin_vector);
           
            print(angle);
            angle=np.mod(360-angle,120)
            print(angle)
            get_output(digitize_output(angle))
            end_time=time.time();
            print("elapsted time is: "+str(float(end_time-start_time))+" in seconds");
            time.sleep(10)
            turn_off_all_ouput_io_pins()

    cap.release();
    cv2.destroyAllWindows();
