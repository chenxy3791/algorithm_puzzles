# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 07:11:00 2021

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
    def cutFruitCake(self, N:int)->(bool,List):
        """
        Given an integer, find one circular permutation of 1...N, satisfying 
        the condition that the sum of each pair of neighbours is one complete 
        square number

        Parameters
        ----------
        N : int. 

        Returns : True or False to indicate whether such circular permutation exists, 
        and if True, the circular permutation        
        -------

        """
        squNum = [k*k for k in range(N)]
        def explore(used, unused):
            if len(used)==N and (used[0]+used[-1]) in squNum:
                # print(used)
                return True, used
            
            cur = used[-1]
            cutOK = False
            for k,nxt in enumerate(unused):
                if cur+nxt in squNum:
                    cutOK,finalCut = explore(used+[nxt], unused[:k]+unused[k+1:])
                    if cutOK:
                        return True,finalCut
            return False,[]
        used = [1]
        unused = [k for k in range(2,N+1)]
        return explore(used,unused)
    
if __name__ == '__main__':        
            
    sln    = Solution()            

    tStart = time.time()
    N = 2
    while (1):    
        cutOK, finalCut = sln.cutFruitCake(N)
        if cutOK:
            break
        print('N = {0}: Fail'.format(N))
        N += 1
        
    tCost  = time.time() - tStart
    print('The minimum integer satisfying the condition is:\nN={0}, tCost = {1:6.3f}(sec)'.format(N,tCost))   
    print('finalCut = {0}'.format(finalCut))   
