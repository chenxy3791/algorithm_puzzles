# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:43:10 2021

@author: chenxy
"""

# import sys
import time
# import datetime
# import math
# import random
# from   typing import List
# from   queue import Queue
# from   collections import deque
import itertools as it
import numpy as np

def move(x: int, y: int)->int:
    '''
    当前算盘上值为cursm时，再加上y需要移动算珠的个数

    Parameters
    ----------
    x : int
        The current number in abacus.
    y : int
        The number to be added.

    Returns
    -------
    int
        The number of abacus-stone being moved in the above operation.

    '''
    # The representation of x
    a1 = 1 if x>=50 else 0
    a2 = (x%50) // 10
    a3 = 1 if (x%10)>=5 else 0
    a4 = x%5

    # The representation of x+y
    z  = x + y
    b1 = 1 if z>=50 else 0
    b2 = (z%50) // 10
    b3 = 1 if (z%10)>=5 else 0
    b4 = z%5    
    
    return z, abs(a1-b1)+abs(a2-b2)+abs(a3-b3)+abs(a4-b4)

#1. Can 10 be considered independently? Need further thinking.
# tStart = time.perf_counter()
# minMoves = 100
# for p in it.permutations(range(1,10)):
#     cursum = 0
#     moves  = 0
#     for k in range(9):
#         cursum, move_tmp = move(cursum,p[k])
#         moves = moves + move_tmp
#     moves += 5 # Finally, adding 10 to 45, requires 5 moves.
#     if minMoves > moves:
#         minMoves = moves
# tCost  = time.perf_counter() - tStart
# print('moves={0}, tCost = {1:6.3f}(sec)'.format(minMoves,tCost))

#2. Brute-force search without consider 10 independently
# tStart = time.perf_counter()
# minMoves = 100
# for p in it.permutations(range(1,11)):
#     cursum = 0
#     moves  = 0
#     for k in range(10):
#         cursum, move_tmp = move(cursum,p[k])
#         moves = moves + move_tmp
#     if minMoves > moves:
#         minMoves = moves
# tCost  = time.perf_counter() - tStart
# print('moves={0}, tCost = {1:6.3f}(sec)'.format(minMoves,tCost))

#3. Recursion + Memoization
memo = dict()
minMoves = 100
def search1(bit10, moves)->int:
    '''   
    Parameters
    ----------
    bit10 : int
        10 bits to represent whether each one of [1,2,...,10] is used.
        bit[0]:1; bit[1]:2; ...; bit[9]:10; 
    moves : number of moves up to now.
    Returns
    -------
        The minimum number of moves needed for the current condition.
    '''
    # print(bit10,moves)
    global minMoves
    if bit10 == 0b11_1111_1111:
        if minMoves > moves:
            minMoves = moves
            return    
        
    if (bit10, moves) in memo:        
        # Already visited, no need to continue.
        return    
    
    cur_sum = 0
    for k in range(10):
        if bit10>>k & 0x1 == 1:
            cur_sum = cur_sum + (k+1)
            
    for k in range(10):
        if bit10>>k & 0x1 == 0:                            
            _,cur_move = move(cur_sum, k+1)            
            search1(bit10|(0x1<<k),cur_move+moves)
    memo[(bit10, moves)] = minMoves
    
tStart = time.perf_counter()
search1(0,0)
tCost  = time.perf_counter() - tStart
print('moves={0}, tCost = {1:6.3f}(sec)'.format(minMoves,tCost))

#4. Recursion + Memoization
memo = dict()
def search2(bit10)->int:
    '''   
    Parameters
    ----------
    bit10 : int
        10 bits to represent whether each one of [1,2,...,10] is used.
        bit[0]:1; bit[1]:2; ...; bit[9]:10; 
    Returns
    -------
        The minimum number of moves needed for the current condition.
    '''
    # print(bit10)
    if bit10 == 0b11_1111_1111:
        return 0   
        
    if bit10 in memo:        
        # Already visited, no need to continue.
        return memo[bit10]   
    
    cur_sum = 0
    for k in range(10):
        if bit10>>k & 0x1 == 1:
            cur_sum = cur_sum + (k+1)
    minMoves = 100            
    for k in range(10):
        if bit10>>k & 0x1 == 0:                            
            _,cur_move = move(cur_sum, k+1)            
            moves = search2(bit10|(0x1<<k))
            if minMoves > (moves + cur_move):
                minMoves = (moves + cur_move)                
    memo[bit10] = minMoves
    return minMoves
    
tStart = time.perf_counter()
minMoves = search2(0)
tCost  = time.perf_counter() - tStart
print('moves={0}, tCost = {1:6.3f}(sec)'.format(minMoves,tCost))
