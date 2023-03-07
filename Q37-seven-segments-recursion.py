# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 07:37:19 2021

@author: chenxy
"""
import sys
import time
import datetime
import math
import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
from   math import sqrt, floor, ceil
import numpy as np

segs = np.array([[1,1,1,1,1,1,0],
        [0,1,1,0,0,0,0],
        [1,1,0,1,1,0,1],
        [1,1,1,1,0,0,1],
        [0,1,1,0,0,1,1],
        [1,0,1,1,0,1,1],
        [1,0,1,1,1,1,1],
        [1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1],
        [1,1,1,1,0,1,1]])
distArray  = dict()
minDistSum = np.sum(segs)
minOrder   = None
    
def initDistArray():
    for i in range(len(segs)):
        for j in range(len(segs)):
            distArray[tuple([i,j])] = np.sum(segs[i] ^ segs[j])

def printDistArray():
    print(distArray)
        
def minToggle_recursion():            
    def recur(visited, toggleSum):
        global minDistSum
        global minOrder
        if len(visited)==10:
            if minDistSum > toggleSum:
                minDistSum = toggleSum
                minOrder   = visited
                return
        for k in range(10):
            if k not in visited:
                dist = distArray[(visited[-1],k)]
                recur(visited+[k],toggleSum+dist)                
        return
    for i in range(10):
        recur([i],0)

def minToggle_recursion2():            
    def recur(visited, prev, toggleSum):
        global minDistSum
        global minOrder
        if len(visited)==10:
            if minDistSum > toggleSum:
                minDistSum = toggleSum
                minOrder   = visited
                return
        for k in range(10):
            if k not in visited:
                visited.add(k)
                dist = distArray[(prev,k)]
                recur(visited,k,toggleSum+dist)                
                visited.remove(k)
        return
    for i in range(10):
        recur({i},i,0)

def minToggle_recursion3():            
    global minDistSum
    def recur(unvisited,prev):
        if len(unvisited)==0:
                return 0
        toggleSum = 0
        for k in unvisited:
            unvisited.remove(k)
            dist = distArray[(prev,k)]
            toggleSum += dist + recur(unvisited,k)                
            unvisited.add(k)
        return toggleSum
    
    unvisited = set([k for k in range(10)])
    for i in range(10):
        unvisited.remove(i)
        toggleSum = recur(unvisited,i)
        unvisited.add(i)
        minDistSum = min(minDistSum,toggleSum)

def minToggle_recursion4():            
    global minDistSum
    memo = dict()
    
    def recur(unvisited,prev):
        if len(unvisited)==0:
                return 0
        if tuple(unvisited+[prev]) in memo:
            return memo[tuple(unvisited+[prev])]
        toggleSum = 63 # Not necessarily, big enough is OK
        for k in unvisited:
            unvisited.remove(k)
            dist = distArray[(prev,k)]
            toggleSum = min(dist + recur(unvisited,k),toggleSum)
            unvisited.append(k)
        memo[tuple(unvisited+[prev])] = toggleSum
        return toggleSum
            
    unvisited = [k for k in range(10)]
    for i in range(10):
        unvisited.remove(i)
        toggleSum = recur(unvisited,i)
        unvisited.append(i)
        minDistSum = min(minDistSum,toggleSum)
                                            
if __name__ == '__main__':        
    
    initDistArray()
    
    # t1 = time.perf_counter()
    # minToggle_recursion()
    # tCost = time.perf_counter() - t1      
    # print('Number of toggles = {0}, order = {1}, tCost = {2:6.3f}sec'.format(minDistSum, minOrder,tCost))  
    
    # t1 = time.perf_counter()
    # minToggle_recursion2()
    # tCost = time.perf_counter() - t1      
    # print('Number of toggles = {0}, order = {1}, tCost = {2:6.3f}sec'.format(minDistSum, minOrder,tCost))      

    # t1 = time.perf_counter()
    # minToggle_recursion3()
    # tCost = time.perf_counter() - t1      
    # print('Number of toggles = {0}, order = {1}, tCost = {2:6.3f}sec'.format(minDistSum, minOrder,tCost))          
                        
    t1 = time.perf_counter()
    minToggle_recursion4()
    tCost = time.perf_counter() - t1      
    print('Number of toggles = {0}, order = {1}, tCost = {2:6.3f}sec'.format(minDistSum, minOrder,tCost))          
        