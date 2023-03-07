# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:49:38 2021

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

memo   = dict()
BIGINT = 10000

def cut_cake(m:int,n:int,who:int,eat:List)->int:
    ''' 
    Parameters
    ----------
    m : int
        Horizontal width of the cake.
    n : int
        Vertical height of the cake.
    who : int
        Who's turn to cut and eat.
    eat : List
        Record the eat quantity of two peoples.

    Returns
    -------
    int
        The minimal cut length.
    '''
    global memo
    # print('cut_cake:', m,n,who)
    if (m,n,who,eat[0],eat[1]) in memo:
        return memo[(m,n,who,eat[0],eat[1])]

    if m==1 and n==1:
        eat[who] = eat[who] + 1
        if eat[0] == eat[1]:
            return 0
        else:
            return BIGINT
    
    mincuts = BIGINT
    # Vertical trial Cut
    for x in range(1,m//2+1): 
        new_m = m-x # Keep the larger part
        new_n = n
        eat_smaller = n * x
        eat[who] += eat_smaller # Eat the smaller part
        cutlen = n + cut_cake(new_m,new_n,1-who,eat)
        eat[who] -= eat_smaller # Recover to the state before the call
        if mincuts > cutlen:
            mincuts = cutlen
    # Horizontal trial cut
    for y in range(1,n//2+1):
        new_m = m
        new_n = n-y  # Keep the larger part
        eat_smaller = m * y
        eat[who] += eat_smaller # Eat the smaller part
        cutlen = m + cut_cake(new_m,new_n,1-who,eat)
        eat[who] -= eat_smaller # Recover to the state before the call
        if mincuts > cutlen:
            mincuts = cutlen            
    memo[(m,n,who,eat[0],eat[1])] = mincuts
    return mincuts

def cut_cake2(m:int,n:int,diff:int)->int:
    ''' 
    Parameters
    ----------
    m : int
        Horizontal width of the cake.
    n : int
        Vertical height of the cake.
    diff : int
        Record the difference of eat quantity between two peoples.

    Returns
    -------
    int
        The minimal cut length, starting from the current state.
    '''
    global memo
    # print('cut_cake:', m,n,who)
    m, n = (n,m) if n>m else (m,n)
    if (m,n,diff) in memo:
        return memo[(m,n,diff)]
    if m==1 and n==1: # Reach the goal.
        if diff == 1:
            return 0
        else:
            memo[(m,n,diff)] = BIGINT
            return BIGINT
    
    mincuts = BIGINT
    # Vertical trial Cut
    for x in range(1,m//2+1): 
        new_m = m-x # Keep the larger part
        new_n = n
        eat_smaller = n * x
        cutlen = n + cut_cake2(new_m,new_n,eat_smaller - diff)
        if mincuts > cutlen:
            mincuts = cutlen
    # Horizontal trial cut
    for y in range(1,n//2+1):
        new_m = m
        new_n = n-y  # Keep the larger part
        eat_smaller = m * y
        cutlen = m + cut_cake2(new_m,new_n,eat_smaller - diff)
        if mincuts > cutlen:
            mincuts = cutlen            
    memo[(m,n,diff)] = mincuts
    return mincuts

M = 30
N = 30
tStart = time.perf_counter()
# mincuts = cut_cake(M,N,0,[0,0])
mincuts = cut_cake2(M,N,0)
tCost  = time.perf_counter() - tStart
print('M={0}, N={1}, mincuts={2}, tCost = {3:6.3f}(sec)'.format(M,N,mincuts,tCost))