# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:38:19 2020

@author: Andrew
"""
import time



with open('DayFiveInput.txt') as f:
    
    input_data = f.read().splitlines() 
    

part_one_start_time = time.perf_counter()


seat_IDs = []

for string_to_fol in input_data:
    
    min_row, max_row, min_col, max_col = 0, 127, 0, 7
    
    instruction_list = list(string_to_fol)
    
    for instruction in instruction_list[:-3]:
        
        if instruction == 'F':
    
            
            max_row = int(max_row - ((max_row - min_row) / 2))
            
        else:
            
            min_row = round(min_row + (max_row - min_row) / 2)
            
    # Always take max_row/col    print(min_row, max_row, instruction)

    for instruction in instruction_list[-3:]:

        if instruction == 'L':
        
            max_col = int(max_col - ((max_col - min_col) / 2))
            
        else:
            
            min_col = round(min_col + ((max_col - min_col) / 2))

        
    seat_IDs.append((max_row * 8) + max_col)


max_seat = max(seat_IDs)
print(max_seat)       
    
part_one_end_time = time.perf_counter()

print(part_one_end_time-part_one_start_time)





part_two_start_time = time.perf_counter()


seat_IDs = sorted(seat_IDs)


for seat_counter in range(0, len(seat_IDs)):
    
    if seat_IDs[seat_counter - 1] - seat_IDs[seat_counter] < -1:
        
        print(seat_counter + seat_IDs[0])

part_two_end_time = time.perf_counter()

print(part_two_end_time - part_two_start_time)