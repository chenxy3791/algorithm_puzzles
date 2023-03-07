# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 08:49:46 2021

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

double_strike = [{1,2},{1,4},{2,3},{3,6},{6,9},{8,9},{7,8},{4,7}]

class Solution:
    def baseball_game(self, unStriked: List)->int:
        """
        Parameters
        ----------
        Returns  :  The number of order of striking
        -------
        """
        memo = dict()        
        def findNext(unStriked):
            global double_strike
            ansLst = []            
            strike2Lst= []
            # Search for all possible double strikes
            for item in it.combinations(unStriked, 2):
                # print(item)
                if set(item) in double_strike:
                    new = unStriked.copy()
                    new.remove(item[0])
                    new.remove(item[1])
                    ansLst.append(new)
                    strike2Lst.append(item)
            
            # Search for all possible single strikes            
            for num in unStriked:
                new = unStriked.copy()
                new.remove(num)
                ansLst.append(new)
            
            # print('findNext: {0}-->{1}'.format(unStriked,ansLst))
            return ansLst
            
        def explore(unStriked):
            """
            unStriked : The list of targets not yet striked            
            Returns   : The number of order of striking
            -------
            """            
            # print(unStriked)
            if len(unStriked) == 0:
                return 1            
            if tuple(unStriked) in memo:
                return memo[tuple(unStriked)]

            count  = 0
            nextUnStriked = findNext(unStriked)            
            for item in nextUnStriked:
                count = count + explore(item)                
            memo[tuple(unStriked)] = count
            return count
        
        return explore(unStriked)

if __name__ == '__main__':        
            
    sln     = Solution()   
    tStart  = time.perf_counter()
    count   = sln.baseball_game([k for k in range(1,10)])
    tCost   = time.perf_counter() - tStart
    print('count = {0}, tCost = {1:6.3f}(sec)'.format(count,tCost))        
    
