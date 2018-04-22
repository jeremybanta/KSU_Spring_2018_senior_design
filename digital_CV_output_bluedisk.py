# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:13:39 2018
@author: Jeremy
"""

import cv2
import numpy as np
from keras.models import load_model
import os
import time
import gc;
import copy;
import theano as th
from keras import backend as K
from os import environ
from importlib import reload


# user defined function to change keras backend
def set_keras_backend(backend):
    if K.backend() != backend:
       environ['KERAS_BACKEND'] = backend
       reload(K)
       assert K.backend() == backend

# call the function with "theano"



def getAngle(pred):       #get predicted angle value in degrees
    
    angle=np.arctan2(pred[:,0],pred[:,1])*180/np.pi
    angle[angle<0]=angle[angle<0]+360
    
    
    return angle


def resize(IM):     #resize image to an image with shape of (227,240,x) x is 1 or 3
    
    return cv2.resize(IM,(227,240))


def getError(pred_angle, actual_angle):   #get error of the predicted angle with the actual angle
    
    difference=actual_angle-pred_angle;
    
    
    return np.abs(np.mod(difference+180,360)-180)


def get_data(path):     #get path of the data to load the picle file
    
    filename=open(path,"rb");
    
    return pickle.load(filename)


def normalize(im):    #normalize image between the values -1 and 1
    
    return 2*np.array([(im-np.min(im))/(np.max(im)-np.min(im))])-1


def segment_blue_disk(Image):
    
    start_time=time.time();                          #time object name start_time

    IM=cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)[:,:,0];   #convert RGB to HSV colorspace only get Hue
    #which corresponds to the true color of a particular image
    IM = cv2.medianBlur(IM,9);                         #compute medianblur with (9,9) kernel size
    IM=cv2.Canny(IM,15,75);                            
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
                    
                    
                return Image[ymin:ymax,xmin:xmax,:];    
    else:
            
        return Image;   





def get_angle_degree_val(num):   #gets the angle in degrees input argument is current test number
    #as an interger
    
    # Capture frame-by-frame
    set_keras_backend("theano")



    model=load_model("model.h5");
    
    
        
        
    cap=cv2.VideoCapture(0);
    ret, frame = cap.read();  #ret true if image is retrived from camera false otherwise
    #frame is the image retrived from the camera
    IMAGE=copy.deepcopy(frame);
    #get a deep copy of fram and assign it to the variable name of IMAGE
    start=time.time();
    #set time object to variable name of start
    IM=segment_blue_disk(frame)
    #set IM to segment blue disk of the current frame
    IM=resize(IM);       #resize the image to size of (227,240)
    IM=normalize(IM)     #normalize the resized image
    pred=model.predict(IM);     #predict the outputs of the image sin(theta),cos(theta) values
    angle=getAngle(pred)[0];        #predict angle value of image in degrees
    angle=np.mod(angle,120)
    #cv2.imwrite("C:\\Users\\Jeremy\\Desktop\\test_run_images\\t"+str(num)+str(angle)+".png",IMAGE)
    print(angle);
     #display angle value to the screen
    end=time.time();
    print(str(float(end-start))+" time in seconds for program to run one disk check ")
    #display the execution time of program to the screen
    cap.release()
    cv2.destroyAllWindows()
    gc.collect();


    if(np.int(angle/15)==8):

        return 7;

    else:

        print(np.int(angle/15))

        return np.int(angle/15);
    
get_angle_degree_val(0);
