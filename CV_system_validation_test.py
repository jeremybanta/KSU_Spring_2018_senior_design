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
    

    theta_degree_vector=[];
    
    for element in theta_degrees:
    
        temp=[element,element+120,element+240];
        temp=np.mod(temp,360)
        temp=np.unique(temp)
        temp=np.array(temp,dtype=np.int16)
        theta_degree_vector.append(temp)
            
            
            
    return theta_degree_vector;
        
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
theta_values=get_same_angle_values(theta_values);

def makeDirectory(number):
    
    directory="C:\\Users\\Jeremy\\Validation_set"+str(number);

    if not os.path.exists(directory):
        os.makedirs(directory)


count1=0

for elements in theta_values:
    
    makeDirectory(count1);
    
    for count in range(3):
    
    
        im=cv2.imread("C:\\Users\\Jeremy\\disk0\\_"+str(elements[count])+".png")
        cv2.imwrite("C:\\Users\\Jeremy\\Validation_set"+str(count1)+"\\"+str(count)+".png",im)
        
    count1=count1+1;
    
del prediction_values
del IM_plot_vector
