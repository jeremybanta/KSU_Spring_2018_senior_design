# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:48:47 2018

@author: Jeremy
"""

for name in dir():
    if not name.startswith('_'):
        del globals()[name]


import cv2
import keyboard
import os
import matplotlib.pyplot as plot
import numpy as np
#This file will yield images to use for producing the training data that will be used as the training set

cap = cv2.VideoCapture(1);
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5);
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5);
number_img=0;


while(True):
    # Capture frame-by-frame
   # ret, frame = cap.read()
    
    success,image = cap.read();
    dst=image;
    #dst = cv2.fastNlMeansDenoisingColored(image,None,15,10,7,21)
    cv2.imshow('frame',dst);
    cv2.waitKey(10);
    
    if keyboard.is_pressed('q'):
        
        break;
    
    
    if(keyboard.is_pressed('s')):
        
        pathname="C:\\Users\\Jeremy\\disk"+str(number_img);
        try:
            if os.path.exists(os.path.dirname(pathname)):
            
                os.remove(pathname);
                
        except:
            
            pass;
            
            
        os.makedirs(pathname);
        cv2.imwrite(pathname+str("\\")+"_0"+".png",dst);
        print(number_img);
        number_img=number_img+1;
        keyboard.release('s');
        

        
# When everything done, release the capture
cap.release();
cv2.destroyAllWindows();