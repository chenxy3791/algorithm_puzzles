# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:40:11 2021

@author: chenxy
"""

import sys
import time
import random
from   typing import List
from   queue import Queue
from   collections import deque

class Solution:
    def numOfLoop(self, N: int) -> List:
        ans = []
        
        def modified_collatz(K):
            isFirst = True
            a   = K
            while 1:
                if a%2 == 0:
                    if isFirst:
                        a = 3*a + 1
                        isFirst = False
                    else:
                        a = a/2
                else:
                    a = 3*a + 1
                
                if a == K:
                    return True # Find one loop in modified collatz iteration
                if a == 1:
                    return False # No loop found in modified collatz iteration
            
        for n in range(2,N,2):
            if modified_collatz(n):
                ans.append(n)
            
        return ans
               
if __name__ == '__main__':        
            
    sln = Solution()    

    tStart = time.time()
    N = 1000000
    ans = sln.numOfLoop(N)
    tCost = time.time() - tStart
    print('N = {0}, numOfLoops = {1}, tCost = {2}(sec)'.format(N, len(ans), tCost))              