# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:35:16 2020

@author: Andrew
"""

import DayTwoCython 
import numpy as np
import time 


input_data = np.loadtxt('InputTwo.txt', dtype = object)


#~~~~~~~~~~~~~~~~~~~~~ Part One ~~~~~~~~~~~~~~~~~~~~#

start_time_one = time.perf_counter()

DayTwoCython.part_one(input_data)

end_time_one = time.perf_counter()

print('Time taken {}s'.format(end_time_one - start_time_one))




start_time_two = time.perf_counter()

DayTwoCython.part_two(input_data)

end_time_two = time.perf_counter()

print('Time taken {}s'.format(end_time_two - start_time_two))
