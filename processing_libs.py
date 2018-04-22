# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:15:23 2018

@author: Jeremy
"""

#preprocessing_libs

import numpy as np
import cv2
import pickle


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


