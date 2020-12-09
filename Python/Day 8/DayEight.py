# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:46:08 2020

@author: Andrew
"""

import time

with open('DayEightInput.txt') as f:
    
    input_data = f.read().splitlines() 
    
    
part_one_start_time = time.perf_counter()

def nop(mag, accumulator, command_counter):
    command_counter += 1
    return accumulator, command_counter

def jump(mag, accumulator, command_counter):
    command_counter += mag
    return accumulator, command_counter

def acc(mag, accumulator, command_counter):
    accumulator += mag
    command_counter += 1
    return accumulator, command_counter


func_dict = {'nop': nop, 'jmp': jump, 'acc': acc}

accumulator = 0

completed_lines = []

command_counter = 0

run = True

while run:

    current_command_line = input_data[command_counter].split(' ')
    
    command = current_command_line[0]
    
    mag = int(current_command_line[1])


    accumulator, command_counter = func_dict[command](mag, accumulator,
                                                      command_counter)

    if command_counter in completed_lines:
        faulty_line = completed_lines[-1]
        run = False
    
    completed_lines.append(command_counter)

print(accumulator)

part_one_end_time = time.perf_counter()

print(part_one_end_time - part_one_start_time,'s')





part_two_start_time = time.perf_counter()

length_input_data = len(input_data)


# 419 as this is the command that caused it to jump to the one already run.



pen_line = length_input_data - 1

swap_dict = {'jmp': 'nop', 'nop':'jmp'}

for possible_faulty_line in completed_lines[:-1]:
    
    test_input_data = input_data.copy()                          


    if test_input_data[possible_faulty_line][:3] != 'acc':
        
        test_input_data[possible_faulty_line] = \
            swap_dict[test_input_data[possible_faulty_line][:3]] + \
                test_input_data[possible_faulty_line][3:]
    else:
    
         continue

    
    
    accumulator = 0
    
    completed_lines = []
    
    command_counter = 0
    
    run = True
    
    
    while run:
    
        current_command_line = test_input_data[command_counter].split(' ')
        
        command = current_command_line[0]
        
        mag = int(current_command_line[1])
    
        
        accumulator, command_counter = func_dict[command](mag, accumulator,
                                                          command_counter)
        
        
        if command_counter in completed_lines:
            
            #print('Faulty line ', completed_lines[-1])
            
            faulty_line = completed_lines[-1]
            
            run = False
            
    
        if command_counter == pen_line:
            
            run = False
            

            
            print(accumulator)
        completed_lines.append(command_counter)
    
    
part_two_end_time = time.perf_counter()


print(part_two_end_time - part_one_end_time, 's')    
    
    












