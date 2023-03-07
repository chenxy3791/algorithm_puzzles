# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 08:24:18 2021

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

N = 6
M = 6
total_count = 0

def f(manX, manY, womanX, womanY, meet):
    # print(manX, manY, womanX, womanY, meet)
    global total_count

    if manX > N or manY > M or womanX < 0 or womanY < 0:
        return # Cross the boundary
    if manX > womanX and manY > womanY:
        return # Missed forever
    
    if manX == womanX and manY == womanY:
        total_count += 1
        # print(total_count)
        return
    if manX == womanX or manY == womanY:
        meet += 1
        if meet == 2:
            total_count += 1
            # print(total_count)
            return
        
    # Four possible move combination of two people
    f(manX+1, manY, womanX-1, womanY, meet)
    f(manX+1, manY, womanX, womanY-1, meet)
    f(manX, manY+1, womanX-1, womanY, meet)
    f(manX, manY+1, womanX, womanY-1, meet)

    # return -- No need, Should not come to this point.

tStart  = time.perf_counter()
f(0, 0, N, M, 0)
tCost  = time.perf_counter() - tStart

print('total_count = {0}, tCost = {1:6.3f}(sec)'.format(total_count,tCost))  