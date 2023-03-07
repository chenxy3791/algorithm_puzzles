# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:05:40 2021

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

def reordering1(N:int):
    maxstep = 0
    for start in it.permutations(range(1,N+1)):
        # print(start)
    
        ordering = list(start)
        step     = 0
        while ordering[0] != 1:
            k = ordering[0]
            # print(k)
            tmp = ordering[0:k]
            tmp.reverse()
            ordering = tmp + ordering[k:]
            step     = step + 1
        if maxstep < step:
            maxstep  = step
            maxstart = start
    return maxstep, maxstart

def reordering2(N:int):
    maxstep = 0
    for start in it.permutations(range(1,N+1)):        
        skip = False
        for i in range(N):
            if start[i] == i+1:
                skip = True
        if skip:
            # Skip and go to the next.
            continue
    
        ordering = list(start)
        step     = 0
        while ordering[0] != 1:
            k = ordering[0]
            # print(k)
            tmp = ordering[0:k]
            tmp.reverse()
            ordering = tmp + ordering[k:]
            step     = step + 1
        if maxstep < step:
            maxstep  = step
            maxstart = start
    return maxstep, maxstart

def reordering3(N: int):
    global maxstep
    global maxstart
    maxstep = 0
    maxstart= None
    def recur(cur, start, step):
        # print(cur)
        global maxstep
        global maxstart
        if cur[0] == 1:            
            if maxstep < step:
                maxstep  = step
                maxstart = start
                # print(cur, maxstep, maxstart)
            return
        k   = cur[0]
        tmp = cur[0:k]
        tmp.reverse()
        nxt = tmp + cur[k:]
        recur(nxt, start, step+1)
    
    for start in it.permutations(range(1,N+1)):        
        skip = False
        for i in range(N):
            if start[i] == i+1:
                skip = True
        if skip:
            # Skip and go to the next.
            continue
        start = list(start)
        recur(start, start, 0)
    return maxstep, maxstart

def reordering4(N: int):

    maxstep = 0
    maxstart= None    
    for start in it.permutations(range(1,N+1)):        
        if start[0] != 1:
            # Skip and go to the next.
            continue

        # For each one of them, perform BFS to find the max distance.
        visited   = set()
        q         = deque()
        q.append((start,0))
        visited.add(start)        
    
        while len(q) > 0:
            cur, step = q.popleft()    
            # print(cur,step)
            for k in range(1,N):
                # Search for the next state 
                if cur[k] == k+1:
                    tmp = list(cur[0:k+1])
                    tmp.reverse()
                    nxt = tuple(tmp + list(cur[k+1:]))
                    if nxt not in visited and nxt[0]!=1:
                        visited.add(nxt)
                        q.append((nxt,step+1))
        
        if maxstep < step:
            maxstep = step
            # maxstart = start
            maxstart = cur # In reverse search, the final state corresponds to the start in forward search
    
    return maxstep, maxstart

if __name__ == '__main__':     

    N = 9
    tStart = time.perf_counter()
    maxstep,maxstart = reordering1(N)
    tCost  = time.perf_counter() - tStart
    print('N={0}, maxstep = {1}, maxstart = {2}, tCost = {3:6.3f}(sec)'.format(N,maxstep,maxstart,tCost))

    tStart = time.perf_counter()
    maxstep,maxstart = reordering2(N)
    tCost  = time.perf_counter() - tStart
    print('N={0}, maxstep = {1}, maxstart = {2}, tCost = {3:6.3f}(sec)'.format(N,maxstep,maxstart,tCost))                

    tStart = time.perf_counter()
    maxstep,maxstart = reordering3(N)
    tCost  = time.perf_counter() - tStart
    print('N={0}, maxstep = {1}, maxstart = {2}, tCost = {3:6.3f}(sec)'.format(N,maxstep,maxstart,tCost))                        
        
    tStart = time.perf_counter()
    maxstep,maxstart = reordering4(N)
    tCost  = time.perf_counter() - tStart
    print('N={0}, maxstep = {1}, maxstart = {2}, tCost = {3:6.3f}(sec)'.format(N,maxstep,maxstart,tCost))            
        
    