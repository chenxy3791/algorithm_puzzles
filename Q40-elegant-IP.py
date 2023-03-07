# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 07:25:27 2021

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
    def elegantIP(self) -> int:
        """
        :ret: The total number of IP satisfying the requirement
        """                
        nums = 0
        rsltLst = []
        for A in range(256):
            for B in range(256):
                Abin = bin(A)[2:]
                Bbin = bin(B)[2:]
                Dbin = Abin[::-1] + (8-len(Abin))*'0'
                Cbin = Bbin[::-1] + (8-len(Bbin))*'0'
                D    = int(Dbin,2)
                C    = int(Cbin,2)
                
                combinedStr = str(A)+str(B)+str(C)+str(D)
                if len(set(combinedStr)) == 10:
                    nums = nums + 1
                    rsltLst.append((A,B,C,D))
                    
        return nums, rsltLst
        
if __name__ == '__main__':        
            
    sln    = Solution()            
    
    tStart = time.time()
    nums, rsltLst = sln.elegantIP()
    tCost  = time.time() - tStart
    print('nums={0}, tCost = {1:6.3f}(sec)'.format(nums,tCost))    
    for item in rsltLst:
        print('{0}'.format(item))
                