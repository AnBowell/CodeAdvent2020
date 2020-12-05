# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:26:10 2020

@author: Andrew
"""


ctypedef numpy.int_t DTYPE_t


def part_one(input_data):
    
    cdef int valid_counter = 0

    for entry in input_data: 
        
        letter_count = entry[-1].count(entry[1][0])
        
        split_entry = entry[0].split('-')
    
        if (letter_count >= int(split_entry[0]) and
            letter_count <= int(split_entry[-1])):
        
            valid_counter += 1
            
    print(valid_counter)
    
    
def part_two(input_data):
    
    cdef valid_counter_2 = 0
    
    cdef Py_ssize_t data_len = input_data.shape[0]
    
    for entry_counter in range(data_len): 
        
        entry = input_data[entry_counter]
        
        split_entry = entry[0].split('-')
    
        pos1 = int(split_entry[0]) - 1
        pos2 = int(split_entry[-1]) - 1
        
        letter_to_find = entry[1][0] 
        
        password = entry[-1]
        
        if (password[pos1] == letter_to_find) is not (password[pos2] == letter_to_find):
        
            valid_counter_2 += 1
        
    print(valid_counter_2)