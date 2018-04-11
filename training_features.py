# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 02:56:01 2018

@author: Jeremy
"""
for name in dir():
    if not name.startswith('_'):
        del globals()[name]

import cv2
import numpy as np
import tensorflow as tf
import keras
import os

#keras deep learning approach using convnets 





