# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 02:31:26 2018

@author: Jeremy
"""




# -*- coding: utf-8 -*-


import numpy as np;
import matplotlib.pyplot as plot;
import cv2;
import gc
import os;
import pickle;
import time;
import segment_blue_disk



os.chdir("C:/Users/Jeremy/")
start=time.time();
pathname="C:\\Users\\Jeremy\\disk";
filename="\\_0.png";
theta_list=[];
how_many_disks=input('enter the number of disks please!! ');
how_many_disks=eval(how_many_disks);
Start_Image_vector=[];

for var in range(0,how_many_disks):
    
    Start_Image_vector.append(cv2.imread(pathname+str(var)+filename));
    

training_IM_list=[];
labels_list=[];
centroid_IM=lambda IM: np.array(np.array(np.shape(IM)),dtype=np.int32);


for var in range(0,int(how_many_disks)):
    t11=time.time();
    initial_IM=Start_Image_vector[var];
    initial_IM=segment_blue_disk.segment_blue_disk(initial_IM);
    center=np.array(centroid_IM(initial_IM)/2,dtype=np.int32);
    center=center[0:2];
    center_0=center;
    center=np.flip(center,0);
    center=tuple(center);
    t22=time.time();
    print(float(t22-t11));
    t33=time.time();
    for theta in range(0,360):
    
        
        M=cv2.getRotationMatrix2D(center,theta,1);
        rot=cv2.warpAffine(initial_IM,M,(initial_IM.shape[1],initial_IM.shape[0]));
        cv2.imwrite("C:\\Users\\Jeremy\\disk"+str(var)+"\\_"+str(theta)+".png",rot);
        rot=cv2.resize(rot,(256,256));
        training_IM_list.append(rot);
        labels_list.append([np.sin(np.radians(theta)),np.cos(np.radians(theta))]);
        theta_list.append(theta);
        gc.collect();

    t44=time.time();
    print(float(t44-t33));

    
labels_list=np.array(labels_list);
file_name=open("training_data.pkl","wb")
pickle.dump((theta_list,training_IM_list,labels_list),file_name)
gc.collect();
end=time.time();

print(end-start)
