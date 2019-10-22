# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:17:04 2019

@author: chamiotk
"""
'''
print('Hello World')

myVariable=0
print('myVariable=', myVariable)'''

# Averaging

'''
- What happens if Som initialization is forgotten ?
The script will work but the result will not be correct

- What can you expect if all the values are below zero ?
Error : divide by 0 is impossible (N keep 0 as value)

'''
import numpy as np
import cv2
import random

def average_above_zero(table):
    ##
    #Function that calculates the table average of positive values
    #Args:
    #    @param table: the list to calculate the average
    #Returns the average 
    #Raises Value error if input param is not a list, if the list is empty and if there's no positive value in table
    if not(isinstance(table,list)):
        raise TypeError('average_above_zero, expected a list as input')
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
        raise ZeroDivisionError('average_above_zero, expected at least 1 positive value')        
    return som/n

def max_value(table):
    ##
    #Function that get the max value with its index
    #Args:
    #    @param table: the list to calculate the max
    #Returns the max value and the index
    #Raises Value error if input param is not a list and if the list is empty
    if not(isinstance(table,list)):
        raise TypeError('max_value, expected a list as input')
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
    #Raises Value error if input param is not a list and if the list is empty
    if not(isinstance(table,list)):
        raise TypeError('reverse_table, expected a list as input')
    if len(table) == 0:
        raise ValueError('reverse_table, expected a non empty list as input')
          
    len_table = len(table)
    turns = int(len_table/2)    
    for i in range(turns):
        temp=table[i]
        opp_id = len_table-i-1 
        table[i]=table[opp_id]
        table[opp_id]=temp
    return table
 
    
def roi_bbox(input_image):
    ##
    #Function that computes the bounding box of an image
    #Args:
    #    @param input_image: the numpy array to compute the bounding box
    #Returns a numpy array (the bounding box [left top, right top, bottom right, bottom left])
    #Raises Value error if input param is not a numpy aray and if the array is empty
    if not(isinstance(input_image,np.ndarray)):
        raise TypeError('roi_bbox, expected a numpy array as input')
    if len(input_image) == 0:
        raise ValueError('roi_bbox, expected a non empty array as input')
    
    shape_row=input_image.shape[0]
    shape_col=input_image.shape[1]
    
    # Initialize max and min values
    min_col_idx=shape_col
    min_row_idx=shape_row
    max_col_idx=0
    max_row_idx=0
    
    for idx_row in range(shape_row):
        for idx_col in range(shape_col):
            pix_val = input_image[idx_row, idx_col]
            if pix_val == 255:
                if idx_col > max_col_idx:
                    max_col_idx = idx_col
                if idx_row > max_row_idx:
                    max_row_idx = idx_row
                if idx_col < min_col_idx:
                    min_col_idx = idx_col
                if idx_row < min_row_idx:
                    min_row_idx = idx_row
    return np.array([[min_row_idx, min_col_idx], [min_row_idx, max_col_idx], [max_row_idx, max_col_idx], [max_row_idx, min_col_idx]])

def random_fill_sparse(table, k):
    ##
    #Function that fills randomly the table by 'X'
    #Args:
    #    @param table: the numpy array to fill
    #    @param k: the number of 'X'
    #Returns a numpy array filled with some 'X'
    #Raises Value error if input param is not a numpy aray, if the array is empty and if k is not an integer
    if not(isinstance(table,np.ndarray)):
        raise TypeError('random_fill_sparse, expected a numpy array as input')
    if len(table) == 0:
        raise ValueError('random_fill_sparse, expected a non empty array as input')
    if not(isinstance(k,int)):
        raise TypeError('random_fill_sparse, expected an integer for param k')

    i=0
    while i < k:
        rand_row = random.randint(0,table.shape[0]-1)
        rand_col = random.randint(0,table.shape[1]-1)
        if table[rand_row,rand_col] != 'X':
            table[rand_row,rand_col] = 'X'
            i += 1
    
    return table

def remove_whitespace(string):
    ##
    # Function that removes whitespace in a string
    # Args:
    #    @param string: the text to remove whitespace
    # Returns the string without whitespace
    # Raises Value error if the string is empty 

    if len(string) == 0:
        raise ValueError('remove_whitespace, expected a non empty string as input')

    string_without_spaces = ""
    len_string = len(string)
    for i in range(len_string):
        if string[i] != " ":
            string_without_spaces += string[i]
    
    return string_without_spaces

def sort_bubble(table):
    ##
    # Function that sorts a table with the bubble method
    # Args:
    #    @param table: the table to sort
    # Returns the sorted table
    # Raises Value error if the table is empty and TypeError if table is not a list
    if not(isinstance(table,list)):
        raise TypeError('sort_bubble, expected a list as input')
    if len(table) == 0:
        raise ValueError('sort_bubble, expected a non empty list as input')
    table_sorted = False
    table_len = len(table) - 1

    while table_sorted != True:
        table_sorted = True
        for i in range(table_len):
            if table[i] > table[i+1]:
                save = table[i+1]
                table[i+1] = table[i]
                table[i] = save
                table_sorted = False
        table_len = table_len - 1
    return table

def sort_selective(table):
    ##
    # Function that sorts a table with the selective method
    # Args:
    #    @param table: the table to sort
    # Returns the sorted table
    # Raises Value error if the table is empty and TypeError if table is not a list
    if not(isinstance(table,list)):
        raise TypeError('sort_selective, expected a list as input')
    if len(table) == 0:
        raise ValueError('sort_selective, expected a non empty list as input')
    exchange = False
    len_table = len(table)
    for i in range(len_table):
        min_index = i
        for j in range(i+1, len_table):
            if table[j] < table[min_index]:
                min_index = j
                exchange = True
        if exchange:
            save = table[i]
            table[i] = table[min_index]
            table[min_index] = save
    return table

''' 
#######################               
#test section
#######################

#tab_list=np.array([1,2,3,-4,6,-9])
tab_list=[1,2,3,-4,6,-9]
#tab_zero=np.zeros(12, dtype=np.int16)

###Average test
print('Average above 0 : {average} '.format(average=average_above_zero(tab_list)))

###Max test
max,index=max_value(tab_list)
print('Max value : {max} at index {index}'.format(max=max,index=index))

###Reverse test
print('Normal : {tab}'.format(tab=tab_list))
print('Reverse : {reverse}'.format(reverse=reverse_table(tab_list)))

###Bounding box test
#mat = np.zeros(100,100)
matrix=np.zeros((10,10),dtype=np.int32)
matrix[3:6, 4:8]=np.ones((3,4), dtype=np.int32)
img=cv2.imread('img.png',0)
#cv2.imshow('read image', img)
#cv2.waitKey()
print('Bounding box : {bbox}'.format(bbox=roi_bbox(img)))

###Random array filling test

#a = np.ones((10,10),dtype=np.uint8)
a = np.ones((10,10), dtype=np.chararray)
a *= ' ' #ascii code for space
print('Fill  : {filled}'.format(filled=random_fill_sparse(a,20)))

###Remove whitespace test
str = "Texte avec des espaces "
print('Remove white space : {str}'.format(str=remove_whitespace(str)))

###Sort bubble test
table = [10, 15, 7, 1, 3, 3, 9]
print("Bubble sort : {table}".format(table=sort_bubble(table)))'''

###Sort selective test
table = [10, 15, 7, 1, 3, 3, 9]
print("Selective sort : {table}".format(table=sort_selective(table)))