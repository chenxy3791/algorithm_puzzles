# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:57:51 2021

@author: chenxy
"""

# import sys
import time
# import datetime
# import math
# import random
from   typing import List
# from   queue import Queue
# from   collections import deque
import itertools as it
import numpy as np

N = 7
cnt_geq_10 = 0
tStart = time.perf_counter()
for pItem in it.permutations(range(1,N+1)):
    # print(pItem)
    lines = []
    for i in range(1,N+1):
        lines.append((i,pItem.index(i)+1))
    
    num_crosspoints = 0
    for i in range(N-1):
        for j in range(i+1,N):
            x1,y1 = lines[i]
            x2,y2 = lines[j]
            if (x2-x1)*(y2-y1) < 0:
                num_crosspoints += 1    
    # if num_crosspItemoints >= 10:
    if num_crosspoints == 10:
        cnt_geq_10 += 1

tCost  = time.perf_counter() - tStart
print('N={0}, cnt_geq_10={1}, tCost = {2:6.3f}(sec)'.format(N,cnt_geq_10,tCost))
        