# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:19:57 2020

@author: Andrew
"""
import numpy as np

import time 

from numba import njit

input_data = np.genfromtxt('DayElevenInput.txt', dtype = str, delimiter =1)



part_one_start_time = time.perf_counter()

@njit(cache=True)
def moving_sqaure(input_array, input_shape) :
    
    return_array = np.zeros(input_shape[0] * input_shape[1]).reshape(input_shape[0],
                                                                     input_shape[1])
    
    for x in range(0,input_shape[0]):
        for y in range(0,input_shape[1]):       
            
            if input_array[x,y] == 2:
                return_array[x,y] = 2
                continue 
            
            if (x == 0) and (y == 0):
                to_count = input_array[:2,:2]
                
            elif (x==0) and (y != 0):
                to_count = input_array[0:x+2,y-1:y+2]
                
            elif (x != 0) and (y == 0):
                to_count = input_array[x-1:x+2,0:y+2]
                
            else:
                to_count = input_array[x-1:x+2,y-1:y+2]
                
            if input_array[x,y] == 1:    
                if np.count_nonzero(to_count==1) - 1 > 3:
                    return_array[x,y] = 0
                else:
                    return_array[x,y] = 1
                
            if input_array[x,y] == 0:
                
                if np.count_nonzero(to_count==1) == 0:
                    
                    return_array[x,y] = 1
                else:
                    return_array[x,y] = 0
        
    return return_array




input_shape = input_data.shape

new_input = np.empty(input_shape,dtype = int)

conv_dict = {'L': 0, '#': 1, '.' :2}

for x in range(0,input_shape[0]):
    for y in range(0,input_shape[1]):    
        
        new_input[x,y] = conv_dict[input_data[x,y]]

updated_array = new_input.copy()

last_updated_array = np.empty(input_shape, dtype=int)


while True:
    
    last_updated_array = updated_array.copy()


    updated_array = moving_sqaure(updated_array.copy(),input_shape)       

    if (updated_array == last_updated_array).all():
        print(np.count_nonzero(updated_array == 1))
        break
       
            

part_one_end_time = time.perf_counter()

print(part_one_end_time - part_one_start_time,'s')
