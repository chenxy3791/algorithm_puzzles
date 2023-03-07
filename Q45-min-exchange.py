# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 07:50:03 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
# import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
import numpy as np

N       = 7
q       = deque()
visited = dict()
q.append((tuple(range(N)),0))
visited[tuple(range(0,N))] = 0

tStart = time.perf_counter()
while len(q) > 0:
    cur,layer = q.popleft()
    for c2 in it.combinations(range(N), 2):
        nxtlst = list(cur)
        nxtlst[c2[0]],nxtlst[c2[1]] = nxtlst[c2[1]],nxtlst[c2[0]]
        nxt = tuple(nxtlst)
        if nxt not in visited:
            visited[nxt] = layer + 1
            q.append((nxt,layer+1))
count = 0
for key in visited:
    count += visited[key]
tCost = time.perf_counter() - tStart
print('N = {0}, count={1}, tCost = {2:6.3f}(sec)'.format(N,count,tCost))   
