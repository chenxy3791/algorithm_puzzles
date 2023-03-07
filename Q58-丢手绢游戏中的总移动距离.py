# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 08:04:30 2021

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

def isTargets(a, target):
    for k in range(len(target)):
        if np.array_equal(a, np.roll(target,k)):
            return True
    return False

N   = 8
s0  = np.arange(1,N+1)  # [1,2,3,...,N]
target = s0[::-1]       # In fact, all the circular shift of it are targets
s1     = s0.copy()
s1[0]  = 0              # [0,2,3,...,N]
q      = deque()
visited = set()
q.append((tuple(s1),N,1,0)) # (states, step, runner, start)
visited.add(tuple(s0))
visited.add(tuple(s1))

# flog  = open("Q58.log", "w")
# flog.write('state, steps, runner, start')

tStart  = time.perf_counter()    
isOK = False
while len(q) > 0:
    cur,step,runner,start = q.popleft()  #used as Queue instead of Stack in BFS.
    # print(cur,step,runner,start)
    # flog.write('{0}, {1}, {2}, {3},\n'.format(cur,step,runner,start))
    if isTargets(cur, target):
        isOK = True
        break
        
    for k in range(N):
        nxt = np.array(cur)
        # interchange between runner and nxt[k]
        nxt_runner = nxt[k]
        nxt[k] = runner

        if tuple(nxt) not in visited:
            visited.add(tuple(nxt))
            curSteps = ((k-start) if (k-start)>=0 else (k-start+N)) + N           
            q.append((tuple(nxt),step+curSteps,nxt_runner,k))

if not isOK:
    print('Fails to reach the target states!')
# flog.close()        

tCost  = time.perf_counter() - tStart
print('N={0}, steps = {1}, tCost = {2:6.3f}(sec)'.format(N,step,tCost))