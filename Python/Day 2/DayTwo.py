# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:21:36 2020

@author: Andrew
"""

import numpy as np
import time



#~~~~~~~~~~~~~~~~~~~~~ Part One ~~~~~~~~~~~~~~~~~~~~#

input_data = np.loadtxt('InputTwo.txt', dtype = object)


start_time_one = time.perf_counter()

valid_counter = 0

for entry in input_data: 
    
    letter_count = entry[-1].count(entry[1][0])
    
    split_entry = entry[0].split('-')

    if (letter_count >= int(split_entry[0]) and
        letter_count <= int(split_entry[-1])):
    
        valid_counter += 1
        
print(valid_counter)

end_time_one = time.perf_counter()

print('Time taken {}s'.format(end_time_one - start_time_one))



































start_time_two = time.perf_counter()

valid_counter_2 = 0

for entry in input_data: 
    
    split_entry = entry[0].split('-')

    pos1 = int(split_entry[0]) - 1
    pos2 = int(split_entry[-1]) - 1
    
    letter_to_find = entry[1][0] 
    
    password = entry[-1]
    
    if (password[pos1] == letter_to_find) is not (password[pos2] == letter_to_find):
    
        valid_counter_2 += 1
        
print(valid_counter_2)

end_time_two = time.perf_counter()
    
print('Time taken {}s'.format(end_time_two - start_time_two))



