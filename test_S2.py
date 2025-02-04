#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: chamiotk
"""

import pytest
import S1_algotools as s1

def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0

####
#   Average unit tests
####

def test_average_correct():
    tab_list=[1,2,3,-4,6,-9] 
    assert s1.average_above_zero(tab_list) == 3
    
def test_average_not_a_list():
    with pytest.raises(TypeError):
        s1.average_above_zero(3)

def test_average_empty_list():
    with pytest.raises(ValueError):
        s1.average_above_zero([])

def test_average_not_a_number_list():
    with pytest.raises(ValueError):
        s1.average_above_zero(["3","e"])
        
def test_average_only_negative_values():
    tab_list = [-1, -6, -4, -6]
    with pytest.raises(ZeroDivisionError):
        s1.average_above_zero(tab_list)
        
####
#   Max value unit tests
####
        
def test_max_value_correct():
    tab_list=[1,2,3,-4,6,-9] 
    assert s1.max_value(tab_list) == (6, 4)
    
def test_max_value_not_a_list():
    with pytest.raises(TypeError):
        s1.max_value(3)
        
def test_max_value_empty_list():
    with pytest.raises(ValueError):
        s1.max_value([])
        
####
#   Reverse table unit tests
####
        
def test_reverse_correct():
    tab_list=[1,2,3,-4,6,-9] 
    assert s1.reverse_table(tab_list) == [-9, 6,-4, 3, 2, 1]
    
def test_reverse_not_a_list():
    with pytest.raises(TypeError):
        s1.reverse_table(3)
        
def test_reverse_empty_list():
    with pytest.raises(ValueError):
        s1.reverse_table([])

####
#   Bounding box unit tests
####
import cv2
import numpy as np

def test_bounding_box_correct():
    img=cv2.imread('img.png',0)
    assert (s1.roi_bbox(img) == np.array([[ 91,  95], [ 91, 523], [434, 523], [434,  95]])).prod()
    
def test_bounding_box_not_a_numpy_array():
    with pytest.raises(TypeError):
        s1.roi_bbox(3)
        
def test_bouding_box_empty_array():
    with pytest.raises(ValueError):
        s1.roi_bbox(np.array([]))
        
####
#   Random fill sparse unit tests
####

def test_random_fill_correct():
    tab_list = np.ones((10,10), dtype=np.chararray)
    tab_list *= ' '
    tab_filled = s1.random_fill_sparse(tab_list,3)
    assert len(np.argwhere(tab_filled=='X')) == 3  
    
def test_random_fill_not_a_numpy_array():
    with pytest.raises(TypeError):
        s1.random_fill_sparse(3,3)

def test_random_fill_empty_list():
    with pytest.raises(ValueError):
        s1.random_fill_sparse(np.array([]),3)

def test_random_fill_not_a_number():
    tab_list = np.array([1,2,3,4,5,6])
    with pytest.raises(TypeError):
        s1.random_fill_sparse(tab_list,"d")
        
####
# Remove whitespace unit tests
####
        
def test_remove_whitespace_correct():
    string = "Texte avec des espaces "
    assert s1.remove_whitespace(string) == "Texteavecdesespaces"
    
def test_remove_whitespace_empty_string():
    string = ""
    with pytest.raises(ValueError):
        s1.remove_whitespace(string)

####
# Bubble sort unit tests
####
def test_bubble_correct():
    tab_list = [10, 15, 7, 1, 3, 3, 9]
    assert s1.sort_bubble(tab_list) == [1, 3, 3, 7, 9, 10, 15]

def test_bubble_not_a_list():
    with pytest.raises(TypeError):
        s1.sort_bubble(3)

def test_bubble_empty_list():
    with pytest.raises(ValueError):
        s1.sort_bubble([])

####
# Selective sort unit tests
####
def test_selective_correct():
    tab_list = [10, 15, 7, 1, 3, 3, 9]
    assert s1.sort_selective(tab_list) == [1, 3, 3, 7, 9, 10, 15]

def test_selective_not_a_list():
    with pytest.raises(TypeError):
        s1.sort_selective(3)

def test_selective_empty_list():
    with pytest.raises(ValueError):
        s1.sort_selective([])