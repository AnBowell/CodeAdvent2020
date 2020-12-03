# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:05:38 2020

@author: Andrew
"""

import numpy as np
import time


the_input = np.loadtxt('DayThreeInput.txt', comments = '?', dtype = object)


start_time_one = time.perf_counter()


line_length = len(the_input[0]) 

x_counter = 0 
tree_counter = 0

for y_counter in range(0, len(the_input)):
    
    if x_counter >= line_length: 
        x_counter += -line_length


    if the_input[y_counter][x_counter] == '#':
        tree_counter += 1


    x_counter += 3

print(tree_counter)

end_time_one = time.perf_counter()

print('Time taken {}s'.format(end_time_one - start_time_one))



start_time_two = time.perf_counter()



total_tree_counter = []

for right, down in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):

    x_counter = 0 
    tree_counter = 0
    
    for y_counter in range(0, len(the_input), down):
        
        if x_counter >= line_length: 
            x_counter += -line_length
    
    
        if the_input[y_counter][x_counter] == '#':
            tree_counter += 1
    
    
        x_counter += right
        
    total_tree_counter.append(tree_counter)
    
    
print(np.prod(np.array(total_tree_counter)))

end_time_two = time.perf_counter()
    
print('Time taken {}s'.format(end_time_two - start_time_two))





