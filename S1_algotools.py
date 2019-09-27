# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:04 2019

@author: chamiotk
"""

print('Hello World')

myVariable=0
print('myVariable=', myVariable)

# Averaging

'''
- What happens if Som initialization is forgotten ?
The script will work but the result will not be correct

- What can you expect if all the values are below zero ?
Error : divide by 0 is impossible (N keep 0 as value)

'''
import numpy as np


def average_above_zero(table):
    ##
    #Function that calculates the table average of positive values
    #Args:
    #    @param table: the list to calculate the average
    #Returns the average 
    #Raises Value error if input param is not a list, if there's no positive value in table
    if not(isinstance(table,list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(table) == 0:
        raise ValueError('average_above_zero, expected a non empty list as input')
    if not(isinstance(table[0], (int,float))):
        raise ValueError('average_above_zero, expected a list of numbers')
    
    som=0
    n=0
    
    for i in range(len(table)):
        if table[i] > 0:
            som += table[i]
            n += 1
    if n==0:
        raise ValueError('average_above_zero, expected at least 1 positive value')        
    return som/n

def max_value(table):
    ##
    #Function that get the max value with its index
    #Args:
    #    @param table: the list to calculate the max
    #Returns the max value and the index
    #Raises Value error if input param is not a list
    if not(isinstance(table,list)):
        raise ValueError('max_value, expected a list as input')
    if len(table) == 0:
        raise ValueError('max_value, expected a non empty list as input')
        
    max=table[0]
    index=0
    for i in range(len(table)):
        if table[i] > max:
            max = table[i]
            index=i
    return max, index

def reverse_table(table):
    ##
    #Function that reverses a table
    #Args:
    #    @param table: the table to reverse
    #Returns the reversed table
    #Raises Value error if input param is not a list
    if not(isinstance(table,list)):
        raise ValueError('reverse_table, expected a list as input')
    if len(table) == 0:
        raise ValueError('reverse_table, expected a non empty list as input')
          
    for i in range(len(table)):
        #save last value of the table
        last_value=table[len(table)-1]
        #remove last value of the table
        table.pop()
        #insert the saved value a the current index
        table.insert(i, last_value)
    return table
 
    
def roi_bbox(input_image):
    if not(isinstance(input_image,np.ndarray)):
        raise ValueError('roi_bbox, expected a numpy array as input')
    if len(input_image) == 0:
        raise ValueError('roi_bbox, expected a non empty array as input')
    bbox = np.array([])
    for i in range(len(input_image)):
        for j in range(len(input_image[i])):
            pixel=input_image[i][j]
            print(pixel)
    #Work in progress
    return 0
    
    
    

#test section
#tab_list=np.array([1,2,3,-4,6,-9])
tab_list=[1,2,3,-4,6,-9]
#tab_zero=np.zeros(12, dtype=np.int16)

print('Average above 0 : {average} '.format(average=average_above_zero(tab_list)))
max,index=max_value(tab_list)
print('Max value : {max} at index {index}'.format(max=max,index=index))
print('Normal : {tab}'.format(tab=tab_list))
print('Reverse : {reverse}'.format(reverse=reverse_table(tab_list)))

image = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0]]) 

print(roi_bbox(image))    