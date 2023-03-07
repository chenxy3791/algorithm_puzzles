# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 07:49:36 2021

@author: chenxy
"""

import sys
import time
import datetime
import random
from   typing import List
from   collections import deque
import itertools as it
import numpy as np

def getnext(cur:tuple)->tuple:
    cur_list = list(cur)
    # print(cur_list)
    c0 = cur[0]
    for k in range(c0):
        cur_list[k] = 7-cur_list[k]
    return tuple(cur_list[c0:] + cur_list[0:c0])

# print(getnext((1,1,6,1,6,1)))

tStart  = time.perf_counter()
cyclic   = set()
acyclic  = set()
for state in it.product([1,2,3,4,5,6],repeat=6):
    # print(state)
    cur = state
    statelst = []
    while 1:
        if (cur in acyclic) or (cur in cyclic):
            for s in statelst:
                acyclic.add(s)
            break
        if cur in statelst:
            beforeCur = True
            while len(statelst) > 0:
                s = statelst.pop(0)
                if s == cur:
                    beforeCur = False
                if beforeCur:
                    acyclic.add(s)
                else:
                    cyclic.add(s)
            break
        statelst.append(cur)
        cur = tuple(getnext(list(cur)))
        # print(cur)

tCost  = time.perf_counter() - tStart

print('total_count = {0}, tCost = {1:6.3f}(sec)'.format(len(acyclic),tCost))                  