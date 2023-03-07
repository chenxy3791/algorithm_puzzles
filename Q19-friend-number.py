# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 08:27:24 2021

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

prime = [2,3,5,7,11,13]

globalMin = prime[-1]*prime[-1]

for p in it.permutations(prime):     
    # print(p)

    nums   = [p[0]*p[0]]
    curmax = nums[0]
    for k in range(1,len(p)):
        nums.append(p[k-1]*p[k])
        curmax = max(curmax,nums[-1])
    nums.append(p[-1]*p[-1])    
    curmax = max(curmax,nums[-1])
    
    if globalMin >= curmax:
        globalMin = curmax 
        maxNums   = nums
       
print('globalMin = {0}, {1}'.format(globalMin, maxNums))    