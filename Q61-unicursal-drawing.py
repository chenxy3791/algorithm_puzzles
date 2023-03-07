# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 07:32:03 2021

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

H = 5 # Height, vertical
W = 6 # Width,  horizontal

# nodes initialization, with a guard band surrounding the original nodes
# The guard band is initialized to '-1' to simplify the judgement processing.
nodes0 = np.zeros((H+2, W+2))
nodes0[0,:] = -1
nodes0[H+1,:] = -1
nodes0[:,0] = -1
nodes0[:,W+1] = -1

count = 0

def dfs(h,w,nodes):
    # print('dfs({0},{1},{2})'.format(h,w,nodes))
    global count
    if np.all(nodes[1:H+1,1:W+1]):
        count = count + 1
        return
    
    if nodes[h-1,w] == 0:
        nodes[h-1,w] = 1
        dfs(h-1,w,nodes)
        nodes[h-1,w] = 0
    if nodes[h+1,w] == 0:
        nodes[h+1,w] = 1
        dfs(h+1,w,nodes)    
        nodes[h+1,w] = 0
    if nodes[h,w-1] == 0:
        nodes[h,w-1] = 1
        dfs(h,w-1,nodes)    
        nodes[h,w-1] = 0
    if nodes[h,w+1] == 0:
        nodes[h,w+1] = 1
        dfs(h,w+1,nodes)    
        nodes[h,w+1] = 0        
    
tStart = time.perf_counter()    
for h in range(1,H+1):
    for w in range(1,W+1):
        cur_nodes = nodes0.copy()
        cur_nodes[h,w] = 1
        dfs(h,w,cur_nodes)
        cur_nodes[h,w] = 0
tCost  = time.perf_counter() - tStart
print('(H,W)=({0},{1}), count = {2}, tCost = {3:6.3f}(sec)'.format(H,W,count,tCost))  
        
    