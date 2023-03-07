# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 17:45:33 2021

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

class Solution:
    def shouNanMoFang1(self, nums: List):
        totalSum = sum(nums)
        # cnts     = []
        targetSum   = 0  # The target sum which has the greatest number of combination sum
        targetCnt   = 0  # The number combination sum of the target sum
     
        for target in range(1,totalSum+1):
            cnt  = 0
            # ansLst = []
        
            for k in range(1,len(nums)+1):
                # print('k = ',k)
                for p in it.combinations(nums,k):
                    p_sum = sum(p)
                    if p_sum == target:
                        cnt += 1
                        # ansLst.append(p)
            if cnt > targetCnt:
                targetCnt = cnt
                targetSum = target
            # cnts.append(cnt)
        return targetSum,targetCnt

    def shouNanMoFang2(self, nums: List):
        
        numCombSum = dict()
        for k in range(1,len(nums)+1):
            for p in it.combinations(nums,k):
                p_sum = sum(p)
                if sum(p) in numCombSum:
                    numCombSum[sum(p)] += 1
                else:
                    numCombSum[sum(p)] = 1
        targetSum = max(numCombSum, key=numCombSum.get)
        targetCnt = numCombSum[targetSum]        
        return targetSum,targetCnt

    def shouNanMoFang3(self, nums: List):
        totalSum     = sum(nums)
        targetCnt    = [0] * (totalSum + 1)
        targetCnt[0] = 1
    
        for n in nums:
            for i in range(totalSum - n, -1, -1):
                targetCnt[i + n] += targetCnt[i]
    
        maxtargetCnt = max(targetCnt)
        return targetCnt.index(maxtargetCnt),maxtargetCnt
            
if __name__ == '__main__':        
            
    sln    = Solution()   

    nums     = [1,14,14,4,11,7,6,9,8,10,10,5,13,2,3,15]
    tStart = time.perf_counter()
    targetSum, targetCnt = sln.shouNanMoFang1(nums)
    tCost  = time.perf_counter() - tStart    
    print('Solution1: len(nums)={0}, targetSum = {1}, targetCnt = {2}, tCost = {3:5.3f}(sec)'\
          .format(len(nums),targetSum,targetCnt,tCost))                                        
    
    tStart = time.perf_counter()
    targetSum, targetCnt = sln.shouNanMoFang2(nums)
    tCost  = time.perf_counter() - tStart    
    print('Solution2: len(nums)={0}, targetSum = {1}, targetCnt = {2}, tCost = {3:5.3f}(sec)'\
          .format(len(nums),targetSum,targetCnt,tCost))      

    tStart = time.perf_counter()
    targetSum, targetCnt = sln.shouNanMoFang3(nums)
    tCost  = time.perf_counter() - tStart    
    print('Solution2: len(nums)={0}, targetSum = {1}, targetCnt = {2}, tCost = {3:5.3f}(sec)'\
          .format(len(nums),targetSum,targetCnt,tCost))      
            
    nums     = [1,14,14,4,11,7,6,9,8,10,10,5,13,2,3,15,34,19,21,44,12,31,47,13,41]    
    tStart = time.perf_counter()
    targetSum, targetCnt = sln.shouNanMoFang2(nums)
    tCost  = time.perf_counter() - tStart    
    print('Solution2: len(nums)={0}, targetSum = {1}, targetCnt = {2}, tCost = {3:5.3f}(sec)'\
          .format(len(nums),targetSum,targetCnt,tCost))      

    tStart = time.perf_counter()
    targetSum, targetCnt = sln.shouNanMoFang3(nums)
    tCost  = time.perf_counter() - tStart    
    print('Solution2: len(nums)={0}, targetSum = {1}, targetCnt = {2}, tCost = {3:5.3f}(sec)'\
          .format(len(nums),targetSum,targetCnt,tCost))      
        
    nums     = [1,14,14,4,11,7,6,9,8,10,10,5,13,2,3,15,34,19,21,44,12,31,47,13,41,\
                2,15,17,5,12,37,26,19,28,20,30]    
    tStart = time.perf_counter()
    targetSum, targetCnt = sln.shouNanMoFang3(nums)
    tCost  = time.perf_counter() - tStart    
    print('Solution2: len(nums)={0}, targetSum = {1}, targetCnt = {2}, tCost = {3:5.3f}(sec)'\
          .format(len(nums),targetSum,targetCnt,tCost))      