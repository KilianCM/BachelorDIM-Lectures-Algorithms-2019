# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:39:33 2019

@author: chamiotk
"""

import cv2
import numpy as np

#img_name="images/fujiyama_volcano.jpg"
img_name="images/4k.jpg"
img_gray=cv2.imread(img_name,0)
img_bgr=cv2.imread(img_name,1)

def invert_colors_manual(input_img):
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
 

#### Test section #############           
                
inverted_colors_img = invert_colors_manual(img_bgr)
cv2.imshow("Inverted colors", inverted_colors_img)
cv2.waitKey()                