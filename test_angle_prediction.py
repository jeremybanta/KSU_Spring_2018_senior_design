# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 07:14:09 2018

@author: Jeremy
"""

import cv2
from keras import load_model
import numpy as np
from keras import backend as K
from importlib import reload
import os



os.chdir("C:/Users/Jeremy/Desktop/Senior Project Design")

from processing_libs import get_data,normalize,getAngle
from segment_blue_disk import segment_blue_disk

def set_keras_backend(backend):       #change the backend of keras to theano or tensorflow

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend;
        reload(K);
        assert K.backend() == backend;
        
        
set_keras_backend("theano");


model=load_model("experimental_model.h5");

cap=cv2.VideoCapture(0)
ret,frame=cap.read();

if ret:
    
    cv2.imshow('frame',frame);
    
frame=segment_blue_disk(frame);
frame=normalize(frame);
frame=cv2.resize(frame)
print("angle estimated value is: "+str(getAngle(model.predict(frame))))

