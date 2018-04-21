# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:09:29 2018

@author: Jeremy
"""

from Computer_Vision_video_test import get_angle_degree_val

import cv2
import numpy as np


cap=cv2.VideoCapture(1);

num=input("enter trial run please!!! ");   #asks user to input the number of current trial run 
get_angle_degree_val(eval(num),cap);           #get angle_degree_val of trial run
