# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 07:40:01 2018
@author: Jeremy
"""

import segment_blue_disk;
import numpy as np


shape_vector=[];


def get_resize_box_size(shapes_list):   #get_resize_box_size
    
    
    shapes_list=np.array(shapes_list);
    shapes_list=np.transpose(shapes_list);
    rows=np.average(shapes_list[0]);
    cols=np.average(shapes_list[1]);
    
    
    return (round(rows),round(cols))
    
    

for var in range(0,14): 

    try:

        shape_vector.append(segment_blue_disk.main_test(var)); #get each image added to list
        
    except:
        
        pass;
    
    
resize_image_size=list(get_resize_box_size(shape_vector)) #resized image list