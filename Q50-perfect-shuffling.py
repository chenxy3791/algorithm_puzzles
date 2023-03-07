# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:33:11 2021

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
# import itertools as it
import numpy as np

N = 100

ok_list = []

tStart = time.perf_counter()
for n in range(1,N+1):
    start = np.arange(2*n)
    p     = np.zeros_like(start)
    for k in range(n):
        p[2*k]   = start[k]
        p[2*k+1] = start[n+k]
    # print(p)
    
    cur = start
    cnt = 0
    # recover = False
    while 1:
        cur = cur[p]
        cnt = cnt + 1
        if np.array_equal(cur, start):
            # print(n, cur, start, cnt)
            # if (2*(n-1) % cnt) == 0:
            if (2*(n-1)) == cnt:
                # print(n, cur, start, cnt)
                # recover = True
                ok_list.append(n)
                break
        if cnt > 2*(n-1):
            break
    # if recover:
        # ok_list.append(n)
tCost  = time.perf_counter() - tStart
        
print('length of ok_list = {0}, tCost = {1:6.3f}(sec)'.format(len(ok_list),tCost))
print(ok_list)        
    

