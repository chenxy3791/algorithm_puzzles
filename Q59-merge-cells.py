# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 08:23:03 2021

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

H = 4 # Height, vertical
W = 4 # Width,  horizontal

# cells initialization, with a guard band surrounding the original cells
# The guard band is initialized to '-1' to simplify the judgement processing.
cells = np.zeros((H+2, W+2))
cells[0,:] = -1
cells[H+1,:] = -1
cells[:,0] = -1
cells[:,W+1] = -1

count = 0

def combine_cells(h,w)->int:
    '''
    Parameters
    ----------
    (h,w) : The current exploration point. 
            h represents row index, w represents col index.
    Returns: int
        The number of total arrangement starting from the point (h,w), together 
        with the current cells status, which is a global variable

    '''        
    global count
    
    # print(h,w,idx)
    if   h == H + 1:
        count = count + 1
        # print(cells)    
    elif w == W + 1: 
        # Reach the right boundary, go to explore the next row from the left 
        combine_cells(h+1, 1)
    elif cells[h,w] > 0: 
        # This grid has been occupied, move to the right one
        combine_cells(h, w+1)
    else:
        for i in range(h,H+1):
            for j in range(w,W+1):
                # Judge whether (h,w)--(i,j) ractangulat can be combined.
                # Here, (h,w) represents top-left corner, (i,j) represent right-down corner
                if ~np.any(cells[h:i+1,w:j+1]):
                    cells[h:i+1,w:j+1] = 1
                    combine_cells(h, j+1)
                    cells[h:i+1,w:j+1] = 0
                            
tStart = time.perf_counter()
combine_cells(1, 1)
tCost  = time.perf_counter() - tStart
print('count = {0}, tCost = {1:6.3f}(sec)'.format(count,tCost))  