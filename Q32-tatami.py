# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:18:04 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
# import random
from   typing import List
# from   queue import Queue
# from   collections import deque
import itertools as it
import numpy as np

H = 4 # Heigth of the room
W = 7 # Weigth of the room

# room initialization, with a guard band surrounding the original room
# The guard band is initialized to '-1' to simplify the judgement processing.
room = np.zeros((H+2, W+2))
room[0,:] = -1
room[H+1,:] = -1
room[:,0] = -1
room[:,W+1] = -1

count = 0

def setTatami_rowscan(h,w,idx)->int:
    '''
    Parameters
    ----------
    (h,w) : The current exploration point. h represents row number, w represents col number.
    idx   : The identifier index of Tatami to be arranged.

    Returns: int
        The number of total arrangement from the input condition.

    '''        
    global count
    
    # print(h,w,idx)
    if   h == H + 1:
        count = count + 1
        print(room)    
    elif w == W + 1: 
        # Reach the right boundary, go to explore the next row from the left 
        setTatami_rowscan(h+1, 1, idx)
    elif room[h,w] > 0: 
        # This grid has been occupied, move to the right one
        setTatami_rowscan(h, w+1, idx)
    elif room[h-1,w]==room[h-1,w-1] or room[h,w-1]==room[h-1,w-1]:
        # if (the same IDX for up and left-up) or (the same IDX for left and left-up), 
        # Tatami arrangement is allowed.
        if room[h,w+1]==0: 
            # Horizontal arrangement is allowed
            room[h,w]   = idx
            room[h,w+1] = idx
            setTatami_rowscan(h, w+2, idx+1)
            room[h,w]   = 0
            room[h,w+1] = 0            
        if room[h+1,w]==0:
            # Vertical arrangement is allowed
            room[h,w]   = idx
            room[h+1,w] = idx
            setTatami_rowscan(h, w+1, idx+1)        
            room[h,w]   = 0
            room[h+1,w] = 0

tStart = time.perf_counter()
setTatami_rowscan(1, 1, 1)
tCost  = time.perf_counter() - tStart
print('count = {0}, tCost = {1:6.3f}(sec)'.format(count,tCost))  
                
    