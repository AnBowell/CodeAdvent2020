# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:03:52 2020

@author: Andrew
"""

import numpy as np
import time
from numba import njit

input_data = np.loadtxt('InputOne.txt', dtype = int)


# Part One

@njit(cache=True)
def part_one(input_data):
    for x in input_data:
        for y in input_data:
            if x + y == 2020:
                print(x * y)
                return



part_one_time_start = time.perf_counter()

part_one(input_data)

part_one_time_end = time.perf_counter()

print('This took {}s'.format(part_one_time_end - part_one_time_start))


# Part Two
@njit(cache=True)
def part_two(input_data):
    for x in input_data:
        for y in input_data:
            for z in input_data: 
                if x + y + z == 2020:
                    print(x * y * z)
                    return 

part_two_time_start = time.perf_counter()

# part_two(input_data)
part_two(input_data)


part_two_time_end = time.perf_counter()

print('This took {}s'.format(part_two_time_end - part_two_time_start))