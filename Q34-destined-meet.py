# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 08:24:18 2021

@author: chenxy
"""
import sys
import time
import datetime
import random
from   typing import List
from   collections import deque
import itertools as it
import numpy as np

N = 6
M = 6
total_count = 0

def f(manX, manY, womanX, womanY, meet):
    # print(manX, manY, womanX, womanY, meet)
    global total_count

    if manX > N or manY > M or womanX < 0 or womanY < 0:
        return # Cross the boundary
    # if manX > womanX and manY > womanY:
        # return # Missed forever

    # if manX == N and manY == M and womanX == 0 and womanY == 0:
    # Can be simplied as below:
    if manX == N and manY == M:
        # Both people reach their target respectively, then do the judgement
        if meet >= 2:
            total_count += 1
        return    
    
    if manX == womanX:
        meet += 1
    if manY == womanY:
        meet += 1        
        
    # Four possible move combination of two people
    f(manX+1, manY, womanX-1, womanY, meet)
    f(manX+1, manY, womanX, womanY-1, meet)
    f(manX, manY+1, womanX-1, womanY, meet)
    f(manX, manY+1, womanX, womanY-1, meet)

    return

tStart  = time.perf_counter()
f(0, 0, N, M, 0)
tCost  = time.perf_counter() - tStart

print('total_count = {0}, tCost = {1:6.3f}(sec)'.format(total_count,tCost))  