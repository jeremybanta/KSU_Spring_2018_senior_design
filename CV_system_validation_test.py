# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:08:30 2018

@author: Jeremy
"""

import numpy as np
import cv2
import segment_blue_disk
import os
import gc
import time
import matplotlib.pyplot as plot
import keras
import pickle
from processing_libs import normalize,getAngle,resize
from keras.models import load_model

os.chdir("C:\\Users\\Jeremy");



start_time=time.time();


def get_same_angle_values(theta_degrees):
    
    theta_angle_vector=[];
    increment=0;
    while(True):
        
        theta_degrees=theta_degrees+increment*120;
        
        if len(np.unique(theta_angle_vector))==len(theta_angle_vector):
            
            theta_angle_vector.append(np.mod(theta_degrees,360));
            
        else:
            
            break;
            
    return theta_angle_vector;
        
        

my_index=0;
Image_vector=[];
IM_plot_vector=[];

while(True):
    
    if(not os.path.exists("C:\\Users\\Jeremy\\disk"+str(int(my_index+2))+"\\"+"_0.png")):
        
        
        
        break;
        
    IM=cv2.imread("C:\\Users\\Jeremy\\disk"+str(int(my_index+2))+"\\_0.png");
    IM=segment_blue_disk.segment_blue_disk(IM);
    Image_vector.append(resize(IM))
    IM_plot_vector.append(IM);
    my_index=my_index+1;


Image_vector=normalize(Image_vector);
end_time_pre_process=time.time();

print("elapsted time preprocessing"+" "+str(my_index)+" number of images is: "+
      str(float(end_time_pre_process-start_time))+" seconds")

gc.collect();

Image_vector=Image_vector[0];
comparison_IM_vector=[];




    
for var in range(len(Image_vector)):
    
    
    
    
    
    image=IM_plot_vector[var];
    image=np.flip(image,2);
    plot.figure(var+1);
    plot.imshow(image);

    
gc.collect();   
    
model=load_model("model.h5");
prediction_values=model.predict(Image_vector);
theta_values=getAngle(prediction_values)



    
    





