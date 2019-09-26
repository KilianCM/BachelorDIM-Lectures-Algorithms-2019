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
    #Function that calculates the table average without values < 0
    #Args:
    #    @param table: the list to calculate the average
    #Returns the average 
    som=0
    n=0
    
    for i in range(len(table)):
        if table[i] > 0:
            som += table[i]
            n += 1    
    return som/n

def max_value(table):
    ##
    #Function that get the max value with its index
    #Args:
    #    @param table: the list to calculate the max
    #Returns the max value and the index
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
    for i in range(len(table)):
        #save last value of the table
        last_value=table[len(table)-1]
        #remove last value of the table
        table.pop()
        #insert the saved value a the current index
        table.insert(i, last_value)
    return table
    

#test section
#tab_list=np.array([1,2,3,-4,6,-9])
tab_list=[1,2,3,-4,6,-9]
#tab_zero=np.zeros(12, dtype=np.int16)

print('Average above 0 : {average} '.format(average=average_above_zero(tab_list)))
max,index=max_value(tab_list)
print('Max value : {max} at index {index}'.format(max=max,index=index))
print('Normal : {tab}'.format(tab=tab_list))
print('Reverse : {reverse}'.format(reverse=reverse_table(tab_list)))