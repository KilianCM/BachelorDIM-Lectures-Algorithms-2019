# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:39:33 2019

@author: chamiotk
"""

import cv2
import numpy as np
from timeit import Timer

#img_name="images/fujiyama_volcano.jpg"
img_name="images/4k.jpg"
img_gray=cv2.imread(img_name,0)
img_bgr=cv2.imread(img_name,1)

def invert_colors_manual(input_img):
    ##
    #Function that inverts colors of an image manually
    #Args:
    #    @param input_img: the image to invert
    #Returns the image with inverted colors
    '''
    ####  slooooow ####
    row=input_img.shape[0]
    col=input_img.shape[1]
    channels=input_img.shape[2]
    for i in range(row):
        for j in range(col):
            for channel in range(channels):
                input_img[i,j,channel] = 255 - input_img[i,j,channel]
    return input_img
    ####
    '''
    return 255-input_img        
 
def invert_colors_numpy(input_img):
    ##
    #Function that inverts colors of an image using numpy
    #Args:
    #    @param input_img: the image to invert
    #Returns the image with inverted colors
    return np.invert(input_img)

def invert_colors_cv2(input_img):
    ##
    #Function that inverts colors of an image using cv2
    #Args:
    #    @param input_img: the image to invert
    #Returns the image with inverted colors
    return cv2.bitwise_not(input_img)


#### Test section #############           
                
#inverted_colors_img = invert_colors_manual(img_bgr)
#inverted_colors_img = invert_colors_numpy(img_bgr)
#inverted_colors_img = invert_colors_cv2(img_bgr)
#cv2.imshow("Inverted colors", inverted_colors_img)
#cv2.waitKey()   

t = Timer(lambda: invert_colors_manual(img_bgr))
print(t.timeit(number=1))      

t = Timer(lambda: invert_colors_numpy(img_bgr))
print(t.timeit(number=1)) 

t = Timer(lambda: invert_colors_cv2(img_bgr))
print(t.timeit(number=1))

'''
Results :
0.017358299999955307
0.017614799999932984
0.009377900000004047'''     