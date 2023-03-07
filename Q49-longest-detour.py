# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 07:12:37 2021

@author: chenxy
"""

# import sys
import time
# import datetime
# import math
# import random
# from   typing import List
# from   queue import Queue
from   collections import deque
# import itertools as it
# import numpy as np

n = 5
m = 6
target = (n,m)
maxsteps = 0
H = (n+1)*[0]
V = (m+1)*[0]

def dfs(curpos, H, V, steps):
    # print(curpos, H, V, steps)
    global maxsteps
    if curpos == target:
        if maxsteps < steps:
            maxsteps = steps
    # Up trial
    if curpos[0] > 0 and V[curpos[1]] < 2:
        nxtpos = (curpos[0]-1, curpos[1])
        V[curpos[1]] = V[curpos[1]] + 1
        dfs(nxtpos, H, V, steps+1)
        V[curpos[1]] = V[curpos[1]] - 1
    # Down trial
    if curpos[0] < n and V[curpos[1]] < 2:
        nxtpos = (curpos[0]+1, curpos[1])
        V[curpos[1]] = V[curpos[1]] + 1    
        dfs(nxtpos, H, V, steps+1)
        V[curpos[1]] = V[curpos[1]] - 1    
    # Left trial
    if curpos[1] > 0 and H[curpos[0]] < 2:
        nxtpos = (curpos[0], curpos[1]-1)
        H[curpos[0]] = H[curpos[0]] + 1    
        dfs(nxtpos, H, V, steps+1)
        H[curpos[0]] = H[curpos[0]] - 1    
    # Right trial
    if curpos[1] < m and H[curpos[0]] < 2:
        nxtpos = (curpos[0], curpos[1]+1)
        H[curpos[0]] = H[curpos[0]] + 1        
        dfs(nxtpos, H, V, steps+1)
        H[curpos[0]] = H[curpos[0]] - 1    
    return

tStart  = time.perf_counter()
dfs((0,0),H,V,0)
tCost  = time.perf_counter() - tStart
print('n={0}, m={1}, maxsteps={2}, tCost = {3:6.3f}(sec)'.format(n,m,maxsteps,tCost))

        