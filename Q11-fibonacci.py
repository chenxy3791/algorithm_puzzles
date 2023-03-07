# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:23:22 2021

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
    def fibonacci(self, N: int) -> List:
        """
        :N:   The number of fibonacci number satisfying the condition to be searched
        :ret: The list of fibonacci number satisfying the condition
        """ 

        def digitSum(num):
            """
            :num: Input integer 
            :ret: The sum of the digits of the input integer
            """             
            # Alternative 1
            rslt = sum([int(s) for s in list(str(num))])
            # # Alternative 2
            # rslt = 0
            # while num > 0:
            #     rem   = num % 10
            #     num   = num // 10
            #     rslt += rem
            return rslt
                  
        ans = []          
        prev,cur = 1,1
        k   = 2
        cnt = 0
        while cnt < N:
            prev,cur    = cur,prev+cur
            k           = k + 1
            curDigitSum = digitSum(cur)
            if cur%curDigitSum == 0:
                ans.append((k,cur))
                cnt = cnt + 1
        return ans
            
if __name__ == '__main__':        
            
    sln    = Solution()    

    tStart = time.time()
    N      = 11
    ans    = sln.fibonacci(N)
    tCost  = time.time() - tStart
    print('N={0}, tCost = {1:.3f}(sec)'.format(N,tCost))           
    for item in ans:
        print('k={0:2d}, fibonacci={1}'.format(item[0],item[1]))           