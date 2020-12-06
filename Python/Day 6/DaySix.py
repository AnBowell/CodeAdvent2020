# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:43:28 2020

@author: Andrew
"""
import time

with open('DaySixInput.txt') as f:
    
    input_data = f.read().splitlines() 
    
    
    
part_one_start_time = time.perf_counter()
    
data_len = len(input_data)

person_counter = 0

running_count = 0

for el_counter in range(data_len):
    
    
    if input_data[el_counter] == '' or el_counter == data_len - 1:
        
        
        running_count += len(set(''.join(input_data[el_counter - person_counter : 
                                                    el_counter + 1])))
        
        person_counter = 0
    
    person_counter += 1
    
    
print(running_count)

    
part_one_end_time = time.perf_counter()
    

print(part_one_end_time - part_one_start_time,'s')



part_one_start_time = time.perf_counter()#


data_len = len(input_data)


person_counter = 0

running_count = 0




for el_counter in range(data_len):#range(127,132): # range(0,10):# 
    

    
    if input_data[el_counter] == '' or el_counter == data_len - 1:
        
        
        
        
        group = input_data[el_counter - person_counter : el_counter + 1]
        
      

        group = [i for i in group if i != '']
        
        length_of_group = len(group)

        
        if length_of_group < 2:

            running_count += len(str(group[0]))
            
            person_counter = 0
            
            continue 
        
        

        for char in group[0]:


            
            all_true = []
            
            
            for group_counter in range(length_of_group - 1):

       

                if char in group[group_counter+1]:  
                    # print(True)
                    all_true.append(True)

                else:
                    # print(False)
                    all_true.append(False)
                    break
                    
            # print(all_true)
            # print('Are all true?',all(all_true))
            
            if all(all_true):   
               
                running_count += 1

        
        person_counter = 0
        
        #print(running_count)
        

    
    person_counter += 1
    
    
print(running_count)

    
part_one_end_time = time.perf_counter()
    

print(part_one_end_time - part_one_start_time,'s')