# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:28:06 2021

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
start   = tuple([14,0,0,0,0]) #S0,S1,S2,S3,S4

q       = deque() # Used as Queue for BFS
visited = set()

q.append((start,0))
visited.add(start)

tStart  = time.perf_counter()    
dbg_cnt = 0
teacher_call_and_called_cnt = 0
while len(q) > 0:
    cur,step = q.popleft()    
    dbg_cnt += 1
    if dbg_cnt%10000 == 0:
        print('cur={}, step={}'.format(cur,step))
    # print('cur={}, step={}'.format(cur,step))
    # if dbg_cnt == 10:
    #     break

    s0,s1,s2,s3,s4 = cur
    print('dbg_cnt=',dbg_cnt,cur,s0,s1,s2,s3,s4)
    
    if cur[0]==0 and cur[2] == 0:
        print('Reach the goal!, dbg_cnt = {}'.format(dbg_cnt))
        break

    
    # Teacher wait
    for k in range(min(s0,s1)+1):             # S1 call S0
        for j in range(min(s0-k,s2)+1):       # S2 call S0
            for l in range(min(s0-k-j,s3)+1): # S3 call S0
                s0_nxt = s0 - (k+j+l) # S1 call S0: S0-->S3;
                s1_nxt = s1
                s2_nxt = s2 + k + l
                s3_nxt = s3 + j
                s4_nxt = s4
                nxt = tuple([s0_nxt,s1_nxt,s2_nxt,s3_nxt,s4_nxt])
                if nxt not in visited:
                    q.append((nxt,step+1))
                    visited.add(nxt)
    # Teacher call student in S0 state
    # T_call = False
    for k in range(min(s0-1,s1)+1):
        for j in range(min(s0-k-1,s2)+1):
            for l in range(min(s0-k-j-1,s3)+1):
                s0_nxt = s0 - (k+j+l) - 1
                s1_nxt = s1 + 1
                s2_nxt = s2 + k + l
                s3_nxt = s3 + j
                s4_nxt = s4
                nxt = tuple([s0_nxt,s1_nxt,s2_nxt,s3_nxt,s4_nxt])
                if nxt not in visited:
                    T_call = True
                    q.append((nxt,step+1))
                    visited.add(nxt)    
    # if T_call:
    #     teacher_call_and_called_cnt += 1
        
    # Teacher receives a call from state S2
    # T_called = False
    if s2 > 0:
        for k in range(min(s0,s1)+1):
            for j in range(min(s0-k,s2-1)+1):
                for l in range(min(s0-k-j,s3)+1):
                    s0_nxt = s0 - (k+j+l)
                    s1_nxt = s1
                    s2_nxt = s2 - 1 + l + k
                    s3_nxt = s3 + j
                    s4_nxt = s4 + 1
                    nxt = tuple([s0_nxt,s1_nxt,s2_nxt,s3_nxt,s4_nxt])
                    if nxt not in visited:
                        T_called = True
                        q.append((nxt,step+1))
                        visited.add(nxt)    
    # if T_called:
    #     teacher_call_and_called_cnt += 1
        
tCost  = time.perf_counter() - tStart
print('N={0}, steps = {1}, tCost = {2:6.3f}(sec)'.format(N,step,tCost))
# print('teacher_call_and_called_cnt = {}'.format(teacher_call_and_called_cnt))