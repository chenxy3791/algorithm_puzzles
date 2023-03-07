# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 07:13:17 2021

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

F = dict()
F[1] = {1}
golden_ratio = (math.sqrt(5) + 1)/2
    
def parallel(x,y):
    return x*y/(x+y)

def findValueClosest2GoldenRatio(N):
    for k in range(2,N+1):
        valueSet = set()
        for l in range(1,k//2+1):            
            g1_size = l
            g2_size = k - l            
            
            for e1 in F[g1_size]:
                for e2 in F[g2_size]:
                    valueSet.add(e1+e2)
                    valueSet.add(parallel(e1, e2))
        F[k] = valueSet
        
    # Find the value closest to golden ratio

    valueWithMinDiff = 0
    minDiff      = golden_ratio
    
    for v in F[N]:
        diff = abs(v-golden_ratio)
        if  diff < minDiff:
            minDiff = diff
            valueWithMinDiff = v

    return valueWithMinDiff, F[N]

N = 10
tStart  = time.perf_counter()
valueWithMinDiff, valueSet = findValueClosest2GoldenRatio(N)
tCost   = time.perf_counter() - tStart
print('golden_ratio={0:11.10f}, valueWithMinDiff={1:11.10f}, tCost= {2:6.3f}(sec)'.format(golden_ratio,valueWithMinDiff,tCost))
print('Totally there are {0} kinds value for N = {1} element circuit network'.format(len(valueSet),N))
      
        
    
                
                
