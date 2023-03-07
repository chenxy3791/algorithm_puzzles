# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 07:41:50 2021

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

def paringGame(N:int)->int:
    memo = dict()
    memo[0] = 1
    
    for n in range(2,N+1,2):        
        nums = 0
        for m in range((n//2)):
            # print(n,m)
            nums += memo[2*m] * memo[n-2-2*m]
        memo[n] = nums
        
    return memo[N]

if __name__ == '__main__':        

    for N in range(16,30,4):            
        tStart = time.time()    
        nums = paringGame(N)        
        tCost  = time.time() - tStart
        print('Pairing combination numbers for {0} = {1}, tCost = {2:6.3f}(sec)'.format(N,nums,tCost))                   
        
    