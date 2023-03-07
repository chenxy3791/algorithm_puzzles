# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:52:39 2021

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

memo = dict()

def isFull(pos):
    return np.all(pos[1:7]) and np.all(pos[8:14])

def search(pos):
    
    if tuple(pos) in memo:
        return memo[tuple(pos)]
    if isFull(pos):
        return 1
    
    cnt = 0
    hasSuperEmpty = False
    # Search super empty seat
    for k in [1,2,3,4,5,6,8,9,10,11,12,13]:
        if pos[k]==0 and pos[k-1]!=1 and pos[k+1]!=1:
            pos[k] = 1
            cnt = cnt + search(pos)
            hasSuperEmpty = True
            pos[k] = 0
        
    if not hasSuperEmpty:
        for k in [1,2,3,4,5,6,8,9,10,11,12,13]:
            if pos[k]==0:
                pos[k] = 1
                cnt = cnt + search(pos)
                pos[k] = 0
    memo[tuple(pos)] = cnt
    return cnt

N   = 12 # Can't modify currently
pos = np.zeros(N+3)
pos[N//2+1] = -1
pos[N+2]    = -1

tStart = time.perf_counter()
count = search(pos)
tCost  = time.perf_counter() - tStart
print('count = {0}, tCost = {1:6.3f}(sec)'.format(count,tCost))      