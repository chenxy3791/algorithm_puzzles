# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 08:08:54 2021

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

def expr_gen_eval(n,k,target):    
    op  = ['+', '-', '*', '//','']    
    for ops in it.product(op,repeat = k-1):
        # print(ops)
        exprlist = (2*k-1) * [str(n)]
        for i in range(k-1):
            exprlist[2*i+1] = ops[i]
        exprstr = ''.join(exprlist)
        # print(exprstr)
        rslt = eval(exprstr)
        if rslt == target:
            return True,exprstr
    return False,''

target = 1234
k      = 1
isFound= False
tStart = time.perf_counter()
while 1:
    print('k = {0}'.format(k))
    for n in range(1,10):
        # Forming math expression with k n's and {+,-,*,/,''}
        isFound,exprstr = expr_gen_eval(n, k, target)
        if isFound == True:
            break
    if isFound == True:
        break
    k = k + 1
tCost  = time.perf_counter() - tStart
print('(n,k)=({0},{1}, exprstr={2}, tCost = {3:6.3f}(sec))'.format(n,k,exprstr,tCost))
    
    