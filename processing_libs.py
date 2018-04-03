# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:15:23 2018

@author: Jeremy
"""

#preprocessing_libs

import numpy as np
import cv2
import pickle


def getAngle(pred):
    
    angle=np.arctan2(pred[:,0],pred[:,1])*180/np.pi
    angle[angle<0]=angle[angle<0]+360
    
    
    return angle


def getError(pred_angle, actual_angle):
    
    difference=actual_angle-pred_angle;
    
    
    return np.abs(np.mod(difference+180,360)-180)


def get_data(path):
    
    filename=open(path,"rb");
    
    return pickle.load(filename)


def normalize(im):
    
    return 2*np.array([(im-np.min(im))/(np.max(im)-np.min(im))])-1


