# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 07:59:30 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
# import random
from   typing import List
from   collections import deque
import itertools as it
import numpy as np

hex2gray = dict({0:0})
gray2hex = dict({0:0})
target = 0x80

curhex = target
last   = 0
steps  = 0

tStart = time.perf_counter()
while 1:
    steps += 1
    if curhex not in hex2gray:
        for k in range(last+1,curhex+1):
            # Calculate gray code for k and fill into hex2gray
            k_minus_1_gray = hex2gray[k-1]
            m = 0
            tmp = hex(k_minus_1_gray)
            while 1:                
                if (m == len(tmp)-2) or (m < len(tmp)-2) and (tmp[-1-m] != 'f'):                    
                    k_gray      = k_minus_1_gray + 16**m
                    hex2gray[k] = k_gray
                    gray2hex[k_gray] = k
                    break
                else:
                    m = m + 1
                    
    last   = curhex
    gray   = hex2gray[curhex]
    curhex = gray2hex[gray]
    if curhex == target:
        break
tCost = time.perf_counter() - tStart

print('steps={0}, tCost = {1:6.3f}(sec)'.format(steps,tCost))       
        
            
            
    
