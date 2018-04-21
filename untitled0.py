# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 14:32:57 2017

@author: Jeremy
"""

import math

eps=7./3 - 4./3 -1;

def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")
        


def sqrt_fun(number):
    value=0
    while(pow(value,2)<number):
        value+=1;
    
    value+=1;
    index=0
    while((abs(value-math.sqrt(number)))>eps):
        
        value=(value+(number/value))/2;
        index=index+1;
    
    print(index);
    return value;
        
        
        
        
        
        


num=input('Enter number ');
tic();
num=float(num);
print(sqrt_fun(num));
 
        
number_val=math.sqrt(num);
print('error')
print((number_val-sqrt_fun(num)))
toc();