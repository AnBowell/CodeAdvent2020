# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:20:32 2020

@author: Andrew
"""

import time
import numpy as np
with open('DaySevenInput.txt') as f:
    
    input_data = f.read().splitlines() 
    
    
 
part_one_start_time = time.perf_counter()
bag_dict = {}

# Divisible by 4
    
for element in input_data:
    
    split_el = element.split(' ')
    
    amount_of_words = len(split_el)
    
    outside_bag = ' '.join(split_el[:2])
    
    

    inside_bags = []    
    if amount_of_words % 4 !=0  :
        bag_dict[outside_bag] = inside_bags
        continue 

    

    for word_counter in range(5, amount_of_words,4):
        
        bag = ' '.join(split_el[word_counter:word_counter + 2])
        
        inside_bags.append(bag)
           
    bag_dict[outside_bag] = inside_bags


bag_counter = []
stop = True

matching_keys = ['shiny gold']


def recursive_search(matching_keys, bag_counter):
    
    matching_recursive = []
    
    for match_key in matching_keys:

        for key in bag_dict:
        
            if match_key in bag_dict[key]:
                
                matching_recursive.append(key)
                

    matching_recursive = list(set(matching_recursive))

    bag_counter.extend(matching_recursive)   


    
    if len(matching_recursive) != 0:
        bag_counter = recursive_search(matching_recursive, bag_counter)        

            
    return bag_counter



bag_counter = recursive_search(matching_keys,bag_counter)


print(len(list(set(bag_counter))))
 
part_one_end_time = time.perf_counter()

print(part_one_end_time - part_one_start_time, 's')






# part_one_start_time = time.perf_counter()

# outside_bags, list_of_tups = [], []

# # Divisible by 4
    
# for element in input_data:
    
#     split_el = element.split(' ')
    
    
    
#     amount_of_words = len(split_el)
    
#     outside_bag = ' '.join(split_el[:2])
    
#     outside_bags.append(outside_bag)
    

           
#     inside_bags =[]     
#     if amount_of_words % 4 !=0  :
       
        
#         list_of_tups.append((outside_bag,outside_bag))
#         continue 


    
#     for word_counter in range(5, amount_of_words,4):

#         bag = ' '.join(split_el[word_counter-1:word_counter + 2])
        
#         list_of_tups.append((bag[2:],outside_bag))
           


# # pass 1: create nodes dictionary
# nodes = {}
# for bag in outside_bags:
    
#     nodes[bag] = { 'id': bag}

# # pass 2: create trees and parent-child relations
# forest = []
# for i in list_of_tups:
#     id, parent_id = i
#     node = nodes[id]

#     # either make the node a new tree or link it to its parent
#     if id == parent_id:
#         # start a new tree in the forest
#         forest.append(node)
#     else:
#         # add new_node as child to parent
#         parent = nodes[parent_id]
#         if not 'children' in parent:
#             # ensure parent has a 'children' field
#             parent['children'] = []
#         children = parent['children']
#         children.append(node)

# print(nodes)



# def recursive_key_calling(key):
    
#     key = bag_dict[key]
    
#     print(key)
    
#     if len(key) > 0:
#         recursive_key_calling(key[1][2:])
        

    

# recursive_key_calling('shiny gold')









part_one_start_time = time.perf_counter()

bag_dict = {}

# Divisible by 4
    
for element in input_data:
    
    split_el = element.split(' ')
    
    amount_of_words = len(split_el)
    
    outside_bag = ' '.join(split_el[:2])
    
    

           
    inside_bags =[]     
    if amount_of_words % 4 !=0  :
       
        
        bag_dict[outside_bag] = inside_bags
        continue 


    
    for word_counter in range(5, amount_of_words,4):
        
        
        bag = ' '.join(split_el[word_counter-1:word_counter + 2])
        
        inside_bags.append(bag)
           
    bag_dict[outside_bag] = inside_bags
    


matching_key = ['shiny gold']

running_total = 0

prev_numbers = [1]

# def recursive_filtering(matching_key,running_total,prev_numbers):
    
#     matching_recursive =[]

#     for key in matching_key:
        
        
        
#         for bag in bag_dict[key]:
        
#             number = int(bag[0])
            
            
            
#             to_add = number
#             print(bag,prev_numbers,number)
#             for prev in prev_numbers:
                
#                 to_add *= prev
                
#             #print(to_add)
#             print(to_add)
#             running_total += to_add
            
            
#             prev_numbers.append(number)
            
#             matching_recursive.append(bag[2:])
            
    
#             if len(matching_recursive) != 0:
                
#                 running_total =  recursive_filtering(matching_recursive,running_total,prev_numbers)

#                 prev_numbers = [1]
        
#     return running_total
        
        
# running_total = recursive_filtering(matching_key,running_total,prev_numbers)    

# print(running_total)

keys = ['shiny gold']
prev = [1]
running_tot = 0

recurs_counter = 0

def rec(keys, prev, running_tot, recurs_counter):

    for key in keys:

        print(bag_dict[key])
        
        new_keys = []
        
        for bag in bag_dict[key]:
          
            number = int(bag[0])
            
            print(number)
            
            # running_tot += np.prod(prev) * number
            
            # prev.append(number)
            # print(prev)
            new_keys.append(bag[2:])
            prev.append(number)
            
            
            
            if len(bag_dict[bag[2:]]) > 0:
                recurs_counter += 1
                
                print('Recurs Counter',recurs_counter)
                rec(new_keys, prev, running_tot, recurs_counter)
                
            else:
                #print('Recurs Counter',recurs_counter)
                recurs_counter = 0
           
                print(bag[2:], 'Stopped')
              
rec(keys, prev, running_tot, recurs_counter)
            
            
          