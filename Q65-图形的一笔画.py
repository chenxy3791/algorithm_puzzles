# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:39:28 2021

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

print(__doc__)

H = 3
W = 4
block_degrees = np.array([[2,2,2,2],  # top-left, top-right, bottom-left, bottom-right
                          [3,2,2,3],
                          [2,3,3,2],
                          [3,3,3,3]])

tStart  = time.perf_counter()     
ok_count = 0
for k,cfg in enumerate(it.product([0,1,2,3],repeat=H*W)):    
    # Generate a new board configuration
    board = np.reshape(np.array(cfg),(H,W))
    # print(board)
    if k%100000 == 0:
        print('k = ',k)

    
    # Count the degrees of each vertex
    num_of_odd_degree = 0
    bad_cfg = False
    for i in range(H+1):
        for j in range(W+1):
            if (i,j) == (0,0): # top-left corner vertex
                num_degrees = block_degrees[board[0,0],0]
            elif (i,j) == (0,W):# top-right corner vertex
                num_degrees = block_degrees[board[0,W-1],1]
            elif (i,j) == (H,0):# bottom-left corner vertex
                num_degrees = block_degrees[board[H-1,0],2]
            elif (i,j) == (H,W):# bottom-right corner vertex
                num_degrees = block_degrees[board[H-1,W-1],3]
            elif i==0:#top edge vertexs
                num_degrees = block_degrees[board[0,j-1],1] + block_degrees[board[0,j],0] - 1
            elif i==H:#bottom edge vertexs
                num_degrees = block_degrees[board[H-1,j-1],3] + block_degrees[board[H-1,j],2] - 1
            elif j==0:#left edge vertexs
                num_degrees = block_degrees[board[i-1,0],2] + block_degrees[board[i,0],0] - 1
            elif j==W:#right edge vertexs
                num_degrees = block_degrees[board[i-1,W-1],3] + block_degrees[board[i,W-1],1] - 1
            else: # Interior vertexs
                num_degrees  = block_degrees[board[i-1,j-1],3]  #up-left block
                num_degrees += block_degrees[board[i-1,j],2]    #up-right block
                num_degrees += block_degrees[board[i,j-1],1]    #down-left block
                num_degrees += block_degrees[board[i,j],0]      #down-right block
                num_degrees -= 4
            
            if num_degrees%2 == 1:
                num_of_odd_degree += 1
            if num_of_odd_degree > 2:
                bad_cfg = True
                break
        if bad_cfg:
            break
    if not(bad_cfg or num_of_odd_degree==1):
        ok_count += 1

tCost  = time.perf_counter() - tStart
print('(H,W)=({0},{1}), count={2}, tCost={3:6.3f}(sec)'.format(H,W,ok_count,tCost))
                        