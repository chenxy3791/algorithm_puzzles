# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 07:34:21 2021

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

class Solution:
    def pourWaterGame(self, capacity:List) -> int:
        """
        :A:   The Capacity of cup A
        :B:   The Capacity of cup B
        :C:   The Capacity of cup C
        :ret: The total number of possibale combinations
        """                
        # capacity    = (A,B,C)
        pathHistory = {}
        initState   = [capacity[0],0,0]
        
        def pourWater(curstate, fromCup, toCup):
            """
            pour warter from cup X to cup Y.
            Because curstate is pass-by-reference argument, to avoid it is modified, 
            it should be firstly copied to newstate, and then update newstate.
            Because in the recursiion, the original 'curstate' has its use after return 
            from this call.
            """
            newstate = curstate.copy() # instead of newstate = curstate!
            x = newstate[fromCup]
            y = newstate[toCup]
            Y = capacity[toCup]            
            if x > 0 and y < Y:
                if x+y <= Y:
                    x,y = 0,x+y
                else:
                    x,y = x+y-Y,Y
                newstate[fromCup] = x
                newstate[toCup]   = y
            return newstate
        
        def explore(pathHistory, curstate):
            # Judge whether reach the target state
            if curstate[0] == A/2:
                return 1
            
            # Add curstate to pathHistory
            pathHistory[tuple(curstate)] = ''
            
            nums = 0
            # A --> B
            newstate = pourWater(curstate, 0,1)
            if tuple(newstate) not in pathHistory:
                nums += explore(pathHistory,newstate)
            # A --> C
            newstate = pourWater(curstate, 0,2)
            if tuple(newstate) not in pathHistory:
                nums += explore(pathHistory,newstate)
            # B --> C
            newstate = pourWater(curstate, 1,2)
            if tuple(newstate) not in pathHistory:
                nums += explore(pathHistory,newstate)
            # B --> A
            newstate = pourWater(curstate, 1,0)
            if tuple(newstate) not in pathHistory:
                nums += explore(pathHistory,newstate)            
            # C --> A
            newstate = pourWater(curstate, 2,0)
            if tuple(newstate) not in pathHistory:
                nums += explore(pathHistory,newstate)            
            # C --> B
            newstate = pourWater(curstate, 2,1)
            if tuple(newstate) not in pathHistory:
                nums += explore(pathHistory,newstate)            
            
            pathHistory.pop(tuple(curstate))
            
            return nums
        
        return explore(pathHistory,initState)
                            
if __name__ == '__main__':        
            
    sln    = Solution()    

    numCombination = 0
    for A in range(10,101,2):
        for C in range(1,A//2): # Because it is assumed that B>C
            B = A - C
            if math.gcd(B,C) == 1:
                tStart = time.time()
                ans    = sln.pourWaterGame([A,B,C])
                if ans > 0:
                    numCombination += 1
                tCost  = time.time() - tStart
                print('[A,B,C]=[{0},{1},{2}], ans={3}, tCost = {4:6.3f}(sec)'.format(A,B,C,ans,tCost))
    print('numCombination={0}'.format(numCombination))