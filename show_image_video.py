# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:16:26 2018

@author: Jeremy
"""

import cv2


cap=cv2.VideoCapture(1);

while True:
    
    
    ret,frame=cap.read()
    cv2.imshow('frame',frame);
    cv2.waitKey(0)