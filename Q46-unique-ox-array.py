# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 07:51:03 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
# import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
import numpy as np

N = 4
sigCount = dict()

tStart = time.perf_counter()
for node in it.product([0,1],repeat=N**2):
    a = np.array(node).reshape(N,N)
    # print(a)
    col_sum = np.sum(a,axis=0)
    row_sum = np.sum(a,axis=1)
    sig = tuple(np.concatenate((col_sum,row_sum)))
    if sig in sigCount:
        sigCount[sig] += 1
    else:
        sigCount[sig]  = 1

count = 0
for key in sigCount:
    if sigCount[key] == 1:
        count += 1
tCost = time.perf_counter() - tStart

print('N = {0}, count={1}, tCost = {2:6.3f}(sec)'.format(N,count,tCost))   
