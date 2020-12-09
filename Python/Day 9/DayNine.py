# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:46:46 2020

@author: Andrew
"""

import time

import numpy as np


input_data = np.loadtxt('DayNineInput.txt', dtype=np.int64)

part_one_start_time = time.perf_counter()

preamble_length = 25

for number_counter, number in enumerate(input_data[preamble_length:]):
    
    index = number_counter + preamble_length

    combinations = np.stack(np.meshgrid(input_data[index-preamble_length: index], 
                                        input_data[index-preamble_length: index]),
                                        -1).reshape(-1, 2)

    
    summed_combinations = np.sum(combinations, axis = 1)
    
    divided = summed_combinations/2

    unique_combinations_mask = np.equal(combinations[:,0], divided)
    
    
    
  
    if len(np.where(summed_combinations[~unique_combinations_mask] == number)[0]) == 0:
        invalid_number = number
        print(number)
        break
    
    
part_one_end_counter = time.perf_counter()

print(part_one_end_counter - part_one_start_time,'s')


part_two_start_time = time.perf_counter()

def find_number(input_data):


    for i in range(1, len(input_data)):
        
        for counter in range(i, len(input_data)):
            
            slice_to_add = input_data[counter - i: counter]
            
            
            
            if np.sum(slice_to_add) == invalid_number:
                if i != 1:
                    
                    ordered_slice = sorted(list(slice_to_add))
                    
                    print(ordered_slice[0]+ordered_slice[-1])
                    
                    return None
            
find_number(input_data)
        


part_two_end_counter = time.perf_counter()

print(part_two_end_counter - part_two_start_time,'s')
