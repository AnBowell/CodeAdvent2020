# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:15:06 2020

@author: Andrew
"""

import time 


f = open('DayFourInput.txt', 'r')

input_data = f.readlines()

f.close()


part_one_start_time = time.perf_counter()

filtered_input_data = [y for x in input_data for y in x.split(' ')]

filtered_input_data.append('\n')

valid_passports = 0

field_counter = 0

for element_counter, element in enumerate(filtered_input_data):
    
    field_counter += 1
    
    if element == '\n':
        
        if field_counter - 1 > 7:
            
            valid_passports += 1
        
        if field_counter - 1 == 7:
        
            check_cid_list = filtered_input_data[element_counter - 7: 
                                                 element_counter]
                
    
            if not any('cid:' in field for field in check_cid_list):
                
                valid_passports += 1
                
        field_counter = 0
    
print(valid_passports)

part_one_end_time = time.perf_counter()

print('Time taken: {}s'.format(part_one_end_time - part_one_start_time))






#requirements_dict = {byr}

f = open('DayFourInput.txt', 'r')

input_data = f.readlines()

f.close()



part_two_start_time = time.perf_counter()


def birth_year(input_string):
    
    input_string = int(input_string)

    if input_string < 1920 or input_string > 2002:

        return False
    
    return True
    


def issue_year(input_string):
    
    input_string = int(input_string)

    if input_string < 2010 or input_string > 2020:
        return False
    
    return True


def expiration_year(input_string):
    
    input_string = int(input_string)

    if input_string < 2020 or input_string > 2030:

        return False

    return True
    

def height(input_string):

    if 'cm' in input_string:
            
        if int(input_string[:-2]) < 150 or int(input_string[:-2]) > 193:
        
            return False
        
        return True
        
    elif 'in' in input_string:
        

        
        if int(input_string[:-2]) < 59 or int(input_string[:-2]) > 76:
   
            return False
    
        return True
        
    else: 
        return False


def hair_colour(input_string):
    
    if '#' in input_string:
        
        try:
            int(input_string[1:], 16)
            return True
        
        except:
            print(input_string)
            return False
        
    return False            

def eye_colour(input_string):
    
    if not any(colour in input_string for colour in ['amb', 'blu', 'brn', 'gry','grn', 'hzl', 'oth']):
        
        return False
    
    return True

def passport_ID(input_string):
    
    if len(input_string) != 9:
        return False
        
    return True

def cid(input_string):
    return True
    

lims_dict = {'byr': birth_year, 'iyr': issue_year, 'eyr': expiration_year,
             'hgt': height, 'hcl': hair_colour, 'ecl': eye_colour, 
             'pid': passport_ID,'cid':cid }


filtered_input_data = [y for x in input_data for y in x.split(' ')]

filtered_input_data.append('\n')

valid_passports = 0

field_counter = 0

for element_counter, element in enumerate(filtered_input_data):
    
    field_counter += 1
    
    if element == '\n':
                
        
        if field_counter - 1 > 7:
            
            check_cid_list = filtered_input_data[element_counter - 
                                     (field_counter - 1) :
                                     element_counter]
        
            bool_list = []
            
            for check_el in check_cid_list:
                
                type_value = check_el.split(':')
                
                bool_list.append(lims_dict[type_value[0]](type_value[1].replace('\n','')))
      
            if all(bool_list):

                valid_passports += 1
        
        
        if field_counter - 1 == 7:

            check_cid_list = filtered_input_data[element_counter - 
                                                 (field_counter - 1) :
                                                 element_counter]
                

            if not any('cid:' in field for field in check_cid_list):
                
                
                bool_list = []
                
                for check_el in check_cid_list:
                    
                    type_value = check_el.split(':')
                    
                    bool_list.append(lims_dict[type_value[0]](type_value[1].replace('\n','')))
                    
                if all(bool_list):

                    valid_passports += 1

                
        
    
        field_counter = 0           
                    
                
print(valid_passports)


part_two_end_time = time.perf_counter()

print('Time taken: {}s'.format(part_two_end_time - part_two_start_time))