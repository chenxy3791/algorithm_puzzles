# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:41:49 2021

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
    def candyMisMatch(self, N: int, M: int) -> int:
        """
        :N:    The number of the kinds of candy
        :M:    The number of candied for each kind
        :ret:  The total number of complete-mismatch
        """                
        memo = dict()
        def explore(candy, paper):
            # print('explore:', candy, paper)
            if candy[-1] == 0:
                return 1
            
            if tuple(candy+paper) in memo:
                return memo[tuple(candy+paper)]
            
            for k in range(N):
                if candy[k] > 0:
                    break
            sum = 0
            for j in range(N):
                if j!=k and paper[j]>0:
                    candy[k] -= 1
                    paper[j] -= 1
                    sum += explore(candy,paper)
                    candy[k] += 1
                    paper[j] += 1
            memo[tuple(candy+paper)] = sum
            
            return sum
        return explore(N*[M], N*[M])
                                
if __name__ == '__main__':        
            
    sln    = Solution()    

    N, M   = 5,6
    tStart = time.time()
    ans    = sln.candyMisMatch(N,M)
    tCost  = time.time() - tStart
    print('N={0}, M={1}, ans={2}, tCost={3:6.2f}(sec)'.format(N,M,ans,tCost))
