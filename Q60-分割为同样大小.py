# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 07:31:06 2021

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

def isConnected(grids, color)->bool:    
    # Find the first color-grid, which is flaged as color.
    found = False
    for i in range(H):
        for j in range(W):
            if grids[i+1,j+1] == color:
                start = (i+1,j+1)
                found = True
                break
        if found:
            break
    # print(start)
        
    curGrids = grids.copy()            
    s = deque() # Used as stack, LIFO
    # visited = set() # No need of visited in this problem
    s.append(start)
    # visited.add(start)
    while len(s) > 0:
        cur = s.pop()
        # print(cur)
        curGrids[cur[0],cur[1]] = -1 # Flag it to indicate that it has already been visited.
        if curGrids[cur[0]-1,cur[1]] == color: # Up grid
            s.append((cur[0]-1,cur[1]))
        if curGrids[cur[0]+1,cur[1]] == color: # Down grid
            s.append((cur[0]+1,cur[1]))
        if curGrids[cur[0],cur[1]-1] == color: # Left grid
            s.append((cur[0],cur[1]-1))
        if curGrids[cur[0],cur[1]+1] == color: # Right grid
            s.append((cur[0],cur[1]+1))        
    return not np.any(curGrids==color)


H = 2 # Height, vertical
W = 3 # Width,  horizontal

# nodes initialization, with a guard band surrounding the original nodes
# The guard band is initialized to '-1' to simplify the judgement processing.
nodes0 = np.zeros((H+2, W+2))
nodes0[0,:] = -1
nodes0[H+1,:] = -1
nodes0[:,0] = -1
nodes0[:,W+1] = -1

visited = set()

count = 0

def dfs(h,w,nodes):
    # print('dfs({0},{1},{2})'.format(h,w,nodes))
    global count
    if np.sum(nodes[1:H+1,1:W+1]) == (H*W)//2:
        print(nodes[1:H+1,1:W+1])
        t = tuple(np.reshape(nodes[1:H+1,1:W+1], (H*W,)))
        if t not in visited:            
            # Judge whether all 0-grids are connected.
            if isConnected(nodes,0):
                count = count + 1
            visited.add(t)
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
# STart from top-left grid
nodes0[1,1] = 1
dfs(1,1,nodes0)
tCost  = time.perf_counter() - tStart
print('(H,W)=({0},{1}), count = {2}, tCost = {3:6.3f}(sec)'.format(H,W,count,tCost))  
