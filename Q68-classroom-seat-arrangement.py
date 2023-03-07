# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 07:39:48 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
# import random
from   typing import List
from   collections import deque
import itertools as it
import numpy as np

H = 5 # Height, vertical
W = 6 # Width,  horizontal

# seats initialization, with a guard band surrounding the original seats
# The guard band is initialized to '-1' to simplify the judgement processing.
seats = np.zeros((H+2, W+2))
seats[0,:] = -1
seats[H+1,:] = -1
seats[:,0] = -1
seats[:,W+1] = -1

count = 0

def isNG(h,w):
    if seats[h,w] == -1:
        return False
    return (seats[h+1,w]==seats[h,w] or seats[h+1,w]==-1) and \
           (seats[h-1,w]==seats[h,w] or seats[h-1,w]==-1) and \
           (seats[h,w+1]==seats[h,w] or seats[h,w+1]==-1) and \
           (seats[h,w-1]==seats[h,w] or seats[h,w-1]==-1) 
    

def arrange_seat(h,w, boy, girl)->int:
    '''
    Parameters
    ----------
    (h,w) : The current exploration point. 
            h represents row index, w represents col index.
    Returns: int
        The number of total arrangement starting from the point (h,w), together 
        with the current seats status, which is a global variable

    '''        
    global count
    # print('h = {0}, w = {1}'.format(h,w))
    if   h == H + 1:
        if boy == girl:
            count = count + 1
        # print(seats)    
    elif w == W + 1: # Go to the next row.
        # Reach the right boundary, go to explore the next row from the left 
        arrange_seat(h+1, 1, boy, girl)
    # elif seats[h,w] > 0: 
    #     # This grid has been occupied, move to the right one
    #     arrange_seat(h, w+1)
    else:
        # Try to arrange boy to the current seat(h,w)
        seats[h,w] = 1
        if not (isNG(h-1,w) or isNG(h,w-1) or isNG(h,w)):
            arrange_seat(h,w+1, boy+1, girl)            
        seats[h,w] = 0
        # Try to arrange girl to the current seat(h,w)
        seats[h,w] = 2
        if not (isNG(h-1,w) or isNG(h,w-1) or isNG(h,w)):
            arrange_seat(h,w+1, boy, girl+1)            
        seats[h,w] = 0
                                    
tStart = time.perf_counter()
arrange_seat(1, 1, 0, 0)
tCost  = time.perf_counter() - tStart
print('count = {0}, tCost = {1:6.3f}(sec)'.format(count,tCost))  