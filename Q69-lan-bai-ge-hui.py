# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 07:39:04 2021

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

N = 4
M = 6

seat = np.ones((N,M))
initState1 = seat.copy()
initState1[:,:M//2] = -1
initState2 = seat.copy()
initState2[:,M//2:] = -1
initState3 = seat.copy()
initState3[:N//2,:] = -1
initState4 = seat.copy()
initState4[N//2:,:] = -1

q = deque()
visited = dict()

q.append((tuple(np.reshape(initState1, (N*M,))),0))
q.append((tuple(np.reshape(initState2, (N*M,))),0))
q.append((tuple(np.reshape(initState3, (N*M,))),0))
q.append((tuple(np.reshape(initState4, (N*M,))),0))

visited[tuple(np.reshape(initState1, (N*M,)))] = 0
visited[tuple(np.reshape(initState2, (N*M,)))] = 0
visited[tuple(np.reshape(initState3, (N*M,)))] = 0
visited[tuple(np.reshape(initState4, (N*M,)))] = 0

ansLst = []
tStart = time.perf_counter()
while len(q) > 0:    
    curState, curStep = q.popleft()
    # print(curState,curStep)
    curExt = np.zeros((N+2,M+2))
    curExt[1:N+1,1:M+1] = np.reshape(curState, (N,M))
    for k in range(1,N+1):
        for l in range(1,M+1):
            if curExt[k,l] * curExt[k,l+1] == -1:
                curExt[k,l] *= -1
                curExt[k,l+1] *= -1
                nxtState = curExt[1:N+1,1:M+1]
                if tuple(np.reshape(nxtState, (N*M,))) not in visited:
                    q.append((tuple(np.reshape(nxtState, (N*M,))),curStep+1))
                    visited[tuple(np.reshape(nxtState, (N*M,)))] = curStep+1                    
                curExt[k,l] *= -1
                curExt[k,l+1] *= -1            
            if curExt[k,l] * curExt[k+1,l] == -1:
                curExt[k,l] *= -1
                curExt[k+1,l] *= -1
                nxtState = curExt[1:N+1,1:M+1]
                if tuple(np.reshape(nxtState, (N*M,))) not in visited:
                    q.append((tuple(np.reshape(nxtState, (N*M,))),curStep+1))
                    visited[tuple(np.reshape(nxtState, (N*M,)))] = curStep+1                    
                curExt[k,l] *= -1
                curExt[k+1,l] *= -1


ansSteps = curStep    
numStates = 0
for key in visited:
    if visited[key] == ansSteps:
        ansLst.append(key)
        numStates += 1
tCost  = time.perf_counter() - tStart

print('N={0}, M={1}, ansSteps={2}, numStates={3}, {4:6.3f}(sec)'.format(N,M,ansSteps,numStates,tCost))        
