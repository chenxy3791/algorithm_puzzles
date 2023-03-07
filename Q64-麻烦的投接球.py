# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:39:51 2021

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

N = 12
start      = np.arange(N)
start[-1]  = -1  # Indicated that no ball in hand
target     = np.arange(N)
target[0]  = -1
target[-1] = 0
target     = tuple(target)

throw_dict = dict()
throw_dict[0] = (6,7)
throw_dict[1] = (6,7,8)
throw_dict[2] = (7,8,9)
throw_dict[3] = (8,9,10)
throw_dict[4] = (9,10,11)
throw_dict[5] = (10,11)
throw_dict[6] = (0,1)
throw_dict[7] = (0,1,2)
throw_dict[8] = (1,2,3)
throw_dict[9] = (2,3,4)
throw_dict[10]= (3,4,5)
throw_dict[11]= (4,5)


q = deque() # Used as Queue for BFS
visited = set()

q.append((tuple(start),0))
visited.add(tuple(start))

tStart  = time.perf_counter()    
dbg_cnt = 0
while len(q) > 0:
    cur,step = q.popleft()    
    dbg_cnt += 1
    # if dbg_cnt%1000 == 0:
        # print('cur={}, step={}'.format(cur,step))
    #     break
    if tuple(cur) == target:
        print('Reach the goal!, dbg_cnt = {}'.format(dbg_cnt))
        break
    
    c = np.array(cur)
    empty = np.where(c==-1)[0][0] # Find where is the empty people
    
    for k in throw_dict[empty]:
        # print('empty ={}, throw_set = {}, k={}, cur={}'.format(empty, throw_dict[empty],k,cur))
        nxt = c.copy()
        nxt[empty] = cur[k]
        nxt[k]     = -1
        if tuple(nxt) not in visited:
            visited.add(tuple(nxt))
            q.append((tuple(nxt),step+1))

tCost  = time.perf_counter() - tStart
print('N={0}, steps = {1}, tCost = {2:6.3f}(sec)'.format(N,step,tCost))
    
