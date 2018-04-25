# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 09:02:13 2018

@author: Jeremy
"""


import numpy as np
from operator import itemgetter
import cv2
import os
import pickle
import time
from segment_blue_disk import segment_blue_disk



def get_angle_value(current_image,image_vector):

    
    my_vector=[];
    
    for image in image_vector:
        
        
        my_vector.append(np.abs(np.mean(current_image-image)))
        
        
    return min(enumerate(my_vector), key=itemgetter(1))[0] 


def chdir(pathname):
    
    os.chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");
        
def load_image_list():
    
    
    

    filename=open("blue_disks_grayscale.pkl","rb");   #file name of pickle file of training_data
    return pickle.load(filename)


def process_frame(frame):

    frame=segment_blue_disk(frame)
    frame=cv2.resize(frame,(215,215))
    #frame=cv2.medianBlur(frame,5)
    frame = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    return frame



chdir("C:\\Users\\Jeremy\\Desktop\Senior Project Design");

img_list=load_image_list();

cam = cv2.VideoCapture(1)

cv2.namedWindow("test")

img_counter = 0

while True:
    
    start_time=time.time();
    ret, frame = cam.read()
    
    
    if(ret):
        
        
        
        frame=process_frame(frame)
        angle=get_angle_value(frame,img_list)
        
        
        
        end_time=time.time()
    
        print(np.mod(angle,360))
        print(float(end_time-start_time))
        
        
    
    cv2.imshow("test", frame)
    k=cv2.waitKey(1);
    
    if not ret:
        break
    

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        break;

cam.release()
cv2.destroyAllWindows()




    
    