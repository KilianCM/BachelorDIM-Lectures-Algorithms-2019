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

tab_list=[1,2,3,-4,6,-9]       
        
def test_average_correct():
    assert s1.average_above_zero(tab_list) == 3
    