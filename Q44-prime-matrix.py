# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 07:40:05 2021

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

def isPrime(n: int)->bool:
    if n == 1 or n == 2:
        return True    
    if n%2 == 0:
        return False

    for i in range(2, int(np.sqrt(n)) + 1):
   		if (n % i == 0):
   			return False
    return True    

prime_lst = [] # Used as a stack, oe LIFO
ans_cnt = 0
tStart = time.perf_counter()
for a0 in range(1,10):
    for a1 in range(1,10):
        for a2 in [1,3,7,9]:
            tmp = a0*100+a1*10+a2
            if not isPrime(tmp):
                continue
            prime_lst.append(tmp)
            for a3 in range(1,10):
                for a6 in [1,3,7,9]:
                    tmp = a0*100+a3*10+a6
                    if not (isPrime(tmp) and (tmp not in prime_lst)):
                        continue
                    prime_lst.append(tmp)
                    for a4 in range(0,10):
                        for a5 in [1,3,7,9]:
                            tmp = a3*100+a4*10+a5
                            if not (isPrime(tmp) and (tmp not in prime_lst)):
                                continue
                            prime_lst.append(tmp)
                            for a7 in [1,3,7,9]:
                                tmp = a1*100+a4*10+a7
                                if not (isPrime(tmp) and (tmp not in prime_lst)):
                                    continue
                                prime_lst.append(tmp)
                                for a8 in [1,3,7,9]:
                                    tmp = a2*100+a5*10+a8
                                    if (isPrime(tmp) and (tmp not in prime_lst)):
                                        prime_lst.append(tmp)
                                        tmp = a6*100+a7*10+a8
                                        if (isPrime(tmp) and (tmp not in prime_lst)):
                                            ans_cnt = ans_cnt + 1        
                                        prime_lst.pop()                     
                                prime_lst.pop()
                            prime_lst.pop()
                    prime_lst.pop()
            prime_lst.pop()                                    
tCost  = time.perf_counter() - tStart
print('ans_cnt={0}, tCost = {1:6.3f}(sec)'.format(ans_cnt,tCost))                                            


                
    