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

cap=cv2.VideoCapture(0);   #video capture object to get image from webcam

    
    
define_inputs_and_outputs();  #define inputs and outputs for gpio pins on rpi
    

    
from keras.models import load_model
from processing_libs import getAngle,normalize    #import processing_libs functions getAngle and normalize

model=load_model("model_experemntial.h5");        #load trained keras convolutional neural network

while True:
        
    input()
        
    ret,frame=cap.read();               #read in image from camera (frame)

        
    if(ret):                            #if image recieved from camera
            
        start_time=time.time()         #set start_time object of time.time()
            
        try:                          #try catch error checking to ensure image is not NoneType
                
            frame=segment_blue_disk(frame);  #segment blue disk with hough circles algorithm
            frame=cv2.resize(frame,(215,215)) #resize image from size (x,y) to (215,215)
            
        except:
                
            while True:
                    
                try:
                        
                    print("in the loop now in try except block")
                        
                    frame=segment_blue_disk(frame);
                    frame=cv2.resize(frame,(215,215))
                    break;
                        
                except:
                        
                    continue
                        
        cv2.imshow('frame',frame)    #display frame of image
        cv2.waitKey(1)               #cv2 waitkey
        #frame=cv2.medianBlur(frame,5)
        frame=normalize(frame);        #normalize image pixel values between -1 and 1
        cos_sin_vector=model.predict(np.reshape(frame,(1,215,215,3)));  #reshape image to (1,215,215,3) so keras will not throw error
        angle=getAngle(cos_sin_vector);                                 #vector with columns cos(theta) and sin(theta)
           
        print(angle);                #display angle value on the screen
        angle=np.mod(360-angle,120)   #get clockwise angle in terms of a counterclockwise angle
        print(angle)                         #print clockwise angle value in degrees
        get_output(digitize_output(angle))   #get output and digitize it then send the output to the raspberry pi
        end_time=time.time();                                                        #end time object of type time.time()
        print("elapsted time is: "+str(float(end_time-start_time))+" in seconds");   #display elaspted time of program
        time.sleep(10)                                                               #pause for 10 seconds
        turn_off_all_ouput_io_pins()                                    #turn all output pins off

cap.release();             #release videocapture object
cv2.destroyAllWindows();  #destroy all opencv windows
