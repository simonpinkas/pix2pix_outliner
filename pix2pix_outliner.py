#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:18:03 2018

@author: simonpinkas
"""

import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

nb_test = 50
nb_val = 50

def preprocess_img(file, index):
    print(file)
    img = cv2.imread('./original/'+file, 3)
    res = cv2.resize(img, (150, 100))
    cv2.cvtColor(res, cv2.COLOR_BGR2RGB, res)
    edges = cv2.Canny(res, 60, 60*3)
    edges = cv2.bitwise_not(edges)
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.subplot(121),plt.imshow(res)
    plt.title(''), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title(''), plt.xticks([]), plt.yticks([])

    if index < nb_test:
        savepath = './test/'+ str(index) + '.jpg'
    elif index < nb_test + nb_val:
        savepath = './val/'+ str(index - nb_val) + '.jpg'
    else:
       savepath = './train/'+ str(index - nb_val - nb_test) + '.jpg'
    plt.savefig(savepath, bbox_inches='tight', pad_inches=0)

for index, file in enumerate(os.listdir('./original')):
    if not file.startswith('.'):
        preprocess_img(file, index)
