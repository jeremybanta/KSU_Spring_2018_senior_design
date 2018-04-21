# -*- coding: utf-8 -*-
"""
Spyder Editor

"""


import numpy as np
import keras
import matplotlib.pyplot as plot
from keras.models import load_model
import pickle
import os
import time
import gc;
from processing_libs import getAngle,normalize,getError

os.chdir("C:\\Users\\Jeremy\\Desktop\\Senior Project Design");
start_time=time.time();
plot.close("all")
gc.collect();
model=load_model("model.h5");
gc.collect();
data=pickle.load(open("training_data.pkl","rb"));
validation_Images=data[1];
validation_Images=normalize(validation_Images)[0];
ground_truth_values=data[0];
gc.collect();
del data;

prediction_values=model.predict(validation_Images[0:720]);
theta_angle=getAngle(prediction_values);
error=getError(theta_angle,ground_truth_values);
plot.figure(1);
plot.plot(np.array(ground_truth_values[0:360]),np.array(error[0:360]));
plot.xlabel("ground truth value in degrees");
plot.ylabel("error in prediction angle in degrees");
plot.title("graph of angle estimation error vs ground truth value");
plot.figure(2);
plot.plot(np.array(ground_truth_values[0:360]),np.array(error[360:720]));
plot.xlabel("ground truth value in degrees");
plot.ylabel("error in prediction angle in degrees");
plot.title("graph of angle estimation error vs ground truth value");

print("MAE" +" on the training set is: "+str(float(np.mean(error)))+" in degrees");
end_time=time.time();
print("time elapsed is: "+str(float(end_time-start_time))+"seconds");










