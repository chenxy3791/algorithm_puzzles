# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 07:25:51 2021

@author: chenxy
"""

# import sys
import time
# import datetime
# import math
# import random
# from   typing import List
# from   queue import Queue
# from   collections import deque
import itertools as it
import numpy as np

def flip_sandclock(state0):
    timer   = 0
    state0  = np.array(state0) + 1 # Convert to 1~N
    cur     = state0 
    # print(state0)
    
    visited = set()
    flip_start = 0
    while 1:        
        cur_state  = tuple(list(cur)+[flip_start])
        if cur_state in visited:
            return False, -1  
        visited.add(cur_state)
        
        # 1 minute later
        nxt   = cur - 1 # Using numpy broadcasting
        nxt[nxt<0] = 0 # If no sand in the up half, keep it empty.
        # print(nxt)              
        if np.array_equal(nxt, np.zeros(N,dtype='int')):
            return True, len(visited)
                
        # Flip the sand clocks
        for k in range(flip_start, flip_start + state0[flip_start]):
            m = k%N
            nxt[m] = state0[m] - nxt[m]
        cur = nxt
        flip_start = (flip_start + 1)%N
               
N      = 8
OK_cnt = 0
tStart = time.perf_counter()
for state0 in it.permutations(np.arange(N)):
    rslt, steps = flip_sandclock(state0)
    if rslt    :
        # print(state0, steps)
        OK_cnt += 1
tCost  = time.perf_counter() - tStart
print('N={0}, OK_cnt={1}, tCost = {2:6.3f}(sec)'.format(N,OK_cnt,tCost)) 