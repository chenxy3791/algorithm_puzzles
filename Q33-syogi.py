# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:51:58 2021
@author: chenxy
"""
import sys
import time
import datetime
import math
import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
from   math import sqrt, floor, ceil
import numpy as np
 
N = 9
M = 9
 
total_count = 0
tStart  = time.perf_counter()
for i in range(N*M):
    for j in range(N*M):
        if i==j:
            continue
 
        # Board initialization for each of (fei,jiao) position combination
        board = np.zeros((N+2, M+2),dtype = 'int')        
        board[0,:]   = 2
        board[:,0]   = 2
        board[N+1,:] = 2
        board[:,M+1] = 2
        
        # Convert i,j to 2-D coordinate
        fei_0  = (i//M) + 1
        fei_1  = (i%M)  + 1
        jiao_0 = (j//M) + 1
        jiao_1 = (j%M)  + 1        
        
        # Calculate the grids within Fei's attack range
        # Up direction from the current position
        k = fei_0-1
        while not (board[k,fei_1]==2 or (k,fei_1) == (jiao_0,jiao_1)):
            # if (k,fei_1) != (jiao_0,jiao_1):
            board[k,fei_1] = 1
            k -= 1 # Move up by one grid
        # Down direction from the current position
        k = fei_0+1
        while not (board[k,fei_1]==2 or (k,fei_1) == (jiao_0,jiao_1)):
            board[k,fei_1] = 1
            k += 1 # Move up by one grid
        # Left direction from the current position
        k = fei_1-1
        while not (board[fei_0,k]==2 or (fei_0,k) == (jiao_0,jiao_1)):
            board[fei_0,k] = 1
            k -= 1 # Move left by one grid
        # Right direction from the current position
        k = fei_1+1
        while not (board[fei_0,k]==2 or (fei_0,k) == (jiao_0,jiao_1)):
            board[fei_0,k] = 1
            k += 1 # Move left by one grid
 
        # Calculate the grids within Jiao's attack range
        # Need to handle the repetition removal
        jiao_count = 0
        # Up-Right direction from the current position
        k = jiao_0-1
        l = jiao_1+1
        while not (board[k,l]==2 or (k,l) == (fei_0,fei_1)):
            board[k,l]=1
            k -= 1 
            l += 1
        # Up-Left direction from the current position
        k = jiao_0-1
        l = jiao_1-1
        while not (board[k,l]==2 or (k,l) == (fei_0,fei_1)):
            board[k,l]=1
            k -= 1 
            l -= 1
        # Down-Left direction from the current position
        k = jiao_0+1
        l = jiao_1-1
        while not (board[k,l]==2 or (k,l) == (fei_0,fei_1)):
            board[k,l]=1
            k += 1 
            l -= 1
        # Down-Right direction from the current position
        k = jiao_0+1
        l = jiao_1+1
        while not (board[k,l]==2 or (k,l) == (fei_0,fei_1)):
            board[k,l]=1
            k += 1 
            l += 1
        total_count += np.sum(board[1:N+1,1:N+1])        
tCost  = time.perf_counter() - tStart
print('total_count = {0}, tCost = {1:6.3f}(sec)'.format(total_count,tCost))   