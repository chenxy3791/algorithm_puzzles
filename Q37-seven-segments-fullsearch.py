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


class Solution:
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
    
    def initDistArray(self):
        for i in range(len(self.segs)):
            for j in range(len(self.segs)):
                self.distArray[tuple([i,j])] = np.sum(self.segs[i] ^ self.segs[j])

    def printDistArray(self):
        print(self.distArray)
        
    def minToggle_fullSearch(self):
        for order in it.permutations(list(range(10))):
            # print(order)
            distSum = 0 #np.sum(self.segs[0])
            for k in range(9):
                distSum += self.distArray[(order[k],order[k+1])]
            if self.minDistSum > distSum:
                self.minDistSum = distSum
                self.minOrder = order
        return self.minDistSum, self.minOrder
                        
if __name__ == '__main__':        
    
    sln = Solution()
    sln.initDistArray()
    # sln.printDistArray()        
    
    t1 = time.perf_counter()
    minDistSum, minOrder = sln.minToggle_fullSearch()
    tCost = time.perf_counter() - t1      
    print('Number of toggles = {0}, order = {1}, tCost = {2:6.3f}sec'.format(minDistSum, minOrder,tCost))  
    
                        
        