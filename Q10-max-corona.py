# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 07:14:15 2021
@author: chenxy
"""
 
import sys
import time
import datetime
# import random
from   typing import List
# from   queue import Queue
# from   collections import deque
 
class Solution:
 
    euroRule= [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
    usaRule = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,0,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
    
    def maxSum(self, nums:List, n:int) -> int:
        runningSum = sum(nums[0:n]) # The sum of the first n numbers as initial value
        sumMax     = runningSum
 
        M = len(nums)
        for k in range(1,len(nums)):
            runningSum += nums[(k+n-1)%M] - nums[k-1]
            if sumMax < runningSum:
                sumMax = runningSum
            # print('k ={0},runningSum={1},sumMax={2}'.format(k,runningSum,sumMax))        
        return sumMax
    
    def maxCoronaSum(self, nMin:int, nMax:int) -> List:
        """
        :
        :ret:   The list of numbers satisfying the condition.
        """                
        ans     = []
        
        for n in range(nMin, nMax+1):
            euroMax = self.maxSum(self.euroRule,n)
            usaMax  = self.maxSum(self.usaRule,n)
            # print('n ={0},euroMax={1},usaMax={2}'.format(n,euroMax,usaMax))
                
            if euroMax < usaMax:
                print('n={0}, euroMax={1}, usaSum={2}'.format(n,euroMax,usaMax))
                ans.append(n)
        
        return ans
                
if __name__ == '__main__':        
            
    sln    = Solution()    
 
    tStart = time.time()
    ans    = sln.maxCoronaSum(2,36)
    tCost  = time.time() - tStart
    print('nums ={0}, tCost = {1:6.3f}(sec)'.format(len(ans),tCost))        
    print('ans  ={0}'.format(ans))   
                            