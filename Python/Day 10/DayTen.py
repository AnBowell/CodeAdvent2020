# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:36:25 2020

@author: Andrew
"""

import numpy as np; print(np.prod(np.unique(np.insert(np.diff(np.sort(np.loadtxt('DayTenInput.txt', dtype = int))),[0,-1],[1,3]), return_counts = True)[1]))



#part two -------------------

import itertools


total_combinations = 0

input_data = np.sort(np.loadtxt('DayTenInput.txt', dtype = int))

input_data_with_ends = np.append(input_data,input_data[-1]+3)
input_data_with_ends = np.insert(input_data_with_ends, 0,0)

differences = np.insert(np.diff(input_data_with_ends),0,3)


valid_to_remove_two = []

for el_counter in range(0, len(differences)-1):
    
    if (differences[el_counter] == 3 or differences[el_counter+1] == 3):
    
        valid_to_remove_two.append(False)
    else:
        valid_to_remove_two.append(True)

valid_to_remove_two.append(False)


most_that_can_be_removed_two = np.where(valid_to_remove_two)[0].size

print(most_that_can_be_removed_two)

for k in range(0, most_that_can_be_removed_two + 1):

    amount_of_combinations = (np.math.factorial(most_that_can_be_removed_two) /
                             ((np.math.factorial(most_that_can_be_removed_two - k)
                                                  * np.math.factorial(k))))
    
    total_combinations += amount_of_combinations
    
    print(amount_of_combinations)


# valid_to_remove_three_plus =[]

# for i in range(0, len(differences)):
    
#     if valid_to_remove_two[i-1] and valid_to_remove_two[i+1]:
        
#         valid_to_remove_three_plus.append(False)
        
#     else:
        
#         valid_to_remove_three_plus.append(valid_to_remove_two[i])



# most_that_can_be_removed = np.where(valid_to_remove_three_plus)[0].size

# # print('Most that can be removed is ',most_that_can_be_removed, ' out of ',
# #       len(input_data_with_ends))






# for k in range(2, most_that_can_be_removed + 1):

#     amount_of_combinations = np.math.factorial(most_that_can_be_removed)/((np.math.factorial(most_that_can_be_removed - k)
#                                                   * np.math.factorial(k)))
    
#     total_combinations += amount_of_combinations
    
#     print(amount_of_combinations)



# print(total_combinations)


















# valid_removals = []
# for el_counter in range(1, len(differences) - 1):
    
#     if differences[el_counter + 1] != 3 and differences[el_counter] != 3:
        
#         valid_removals.append(True)
#     else:
#         valid_removals.append(False)
        
# valid_removals.insert(0,False)
# valid_removals.append(False)


# valid_removals = np.array(valid_removals)
# #print(input_data_with_ends[valid_removals])
