# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 07:28:54 2021

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

# grids initialization, with a guard band surrounding the original grids
# The guard band is initialized to '-1' to simplify the judgement processing.
grids = np.zeros((H+2, W+2))
grids[0,:] = -1
grids[H+1,:] = -1
grids[:,0] = -1
grids[:,W+1] = -1

count = 0

def isNG(h,w):
    '''
    '2' represents black.
    Judge whether there are two neighbouring cells are all black

    '''
    return  (grids[h,w]==2) and ((grids[h-1,w]==2) or (grids[h,w-1]==2))

def isAllWhiteConnected(grids)->bool:    
    # Find the first white grid, which is flaged as '1'
    found = False
    for i in range(H):
        for j in range(W):
            if grids[i+1,j+1] == 1:
                start = (i+1,j+1)
                found = True
                break
        if found:
            break
    # print(start)
        
    curGrids = grids.copy()            
    s = deque() # Used as stack, LIFO
    # visited = set() # No need of visited in this problem
    s.append(start)
    # visited.add(start)
    while len(s) > 0:
        cur = s.pop()
        # print(cur)
        curGrids[cur[0],cur[1]] = 0 # Flag it to indicate that it has already been visited.
        if curGrids[cur[0]-1,cur[1]] == 1: # Up grid
            s.append((cur[0]-1,cur[1]))
        if curGrids[cur[0]+1,cur[1]] == 1: # Down grid
            s.append((cur[0]+1,cur[1]))
        if curGrids[cur[0],cur[1]-1] == 1: # Left grid
            s.append((cur[0],cur[1]-1))
        if curGrids[cur[0],cur[1]+1] == 1: # Right grid
            s.append((cur[0],cur[1]+1))        
    return not np.any(curGrids==1)

def arrange_grid(h,w)->int:
    '''
    Parameters
    ----------
    (h,w) : The current exploration point. 
            h represents row index, w represents col index.
    Returns: int
        The number of total arrangement starting from the point (h,w), together 
        with the current grids status, which is a global variable

    '''        
    global count
    # print('h = {0}, w = {1}'.format(h,w))
    if   h == H + 1:
        if isAllWhiteConnected(grids):
            count = count + 1
        # print(grids)    
    elif w == W + 1: # Go to the next row.
        # Reach the right boundary, go to explore the next row from the left 
        arrange_grid(h+1, 1)
    # elif grids[h,w] > 0: 
    #     # This grid has been occupied, move to the right one
    #     arrange_grid(h, w+1)
    else:
        # Try to arrange white to the current grid(h,w). This is always possible
        grids[h,w] = 1
        arrange_grid(h,w+1)            
        grids[h,w] = 0
        # Try to arrange black to the current grid(h,w)
        grids[h,w] = 2
        if not isNG(h,w):
            arrange_grid(h,w+1)            
        grids[h,w] = 0

# # Test of isAllWhiteConnected()
# grids[2,3] = 1
# grids[1,3] = 1
# # print(grids)
# print(isAllWhiteConnected(grids))
                                    
tStart = time.perf_counter()
arrange_grid(1, 1)
tCost  = time.perf_counter() - tStart
print('(H,W)=({0},{1}), count = {2}, tCost = {3:6.3f}(sec)'.format(H,W,count,tCost))  