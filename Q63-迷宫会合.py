# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:34:24 2021

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

print(__doc__)

def is_valid_maze(maze):
    '''
    Check the reachability from [1,1] to [N,N], using BFS algorithm
    '''
    start = (1,1)
    target = (N,N)
        
    curMaze = maze.copy()            
    s = deque() # Used as stack, LIFO
    s.append(start)
    is_valid = False
    while len(s) > 0:
        cur = s.pop()
        if cur == target:
            is_valid = True
        # print(cur)
        curMaze[cur[0],cur[1]] = 0 # Flag it to indicate that it has already been visited.
        if curMaze[cur[0]-1,cur[1]] == 1: # Up grid
            s.append((cur[0]-1,cur[1]))
        if curMaze[cur[0]+1,cur[1]] == 1: # Down grid
            s.append((cur[0]+1,cur[1]))
        if curMaze[cur[0],cur[1]-1] == 1: # Left grid
            s.append((cur[0],cur[1]-1))
        if curMaze[cur[0],cur[1]+1] == 1: # Right grid
            s.append((cur[0],cur[1]+1))        
    return is_valid

def move(A, prev_dir):
    '''
     prev_dir: 0:down, 1: right, 2: up; 3: left
    '''
    if prev_dir == 0: # down 
        if maze[A[0],A[1]-1] == 1: # A left
            A = [A[0],A[1]-1]                    
            A_dir = 3
        elif maze[A[0]+1,A[1]] == 1: # A down
            A = [A[0]+1,A[1]]
            A_dir = 0
        elif maze[A[0],A[1]+1] == 1: # A right
            A = [A[0],A[1]+1]
            A_dir = 1
        else: #if maze[A[0]-1,A[1]] == 1: # A up
            A = [A[0]-1,A[1]]
            A_dir = 2
    elif prev_dir == 1: # right
        if maze[A[0]+1,A[1]] == 1:   # A down
            A = [A[0]+1,A[1]]            
            A_dir = 0
        elif maze[A[0],A[1]+1] == 1: # A right
            A = [A[0],A[1]+1]
            A_dir = 1
        elif maze[A[0]-1,A[1]] == 1: # A up
            A = [A[0]-1,A[1]]
            A_dir = 2
        else: #if maze[A[0],A[1]-1] == 1: # A left
            A = [A[0],A[1]-1]        
            A_dir = 3
    elif prev_dir == 2: # up
        if maze[A[0],A[1]+1] == 1: # A right
            A = [A[0],A[1]+1]
            A_dir = 1
        elif maze[A[0]-1,A[1]] == 1: # A up
            A = [A[0]-1,A[1]]
            A_dir = 2
        elif maze[A[0],A[1]-1] == 1: # A left
            A = [A[0],A[1]-1]                        
            A_dir = 3
        else: #if maze[A[0]+1,A[1]] == 1:   # A down
            A = [A[0]+1,A[1]]            
            A_dir = 0
    elif prev_dir == 3: # left
        if maze[A[0]-1,A[1]] == 1: # A up
            A = [A[0]-1,A[1]]
            A_dir = 2
        elif maze[A[0],A[1]-1] == 1: # A left
            A = [A[0],A[1]-1]                        
            A_dir = 3
        elif maze[A[0]+1,A[1]] == 1: # A down
            A = [A[0]+1,A[1]]                            
            A_dir = 0
        else: #if maze[A[0],A[1]+1] == 1: # A right
            A = [A[0],A[1]+1]                
            A_dir = 1
    return A, A_dir
    
def meet_or_not(maze):
    '''
    A starts from [1,1], B starts from [N,N]
    Can they meet at some grid, by reaching there at the same time?
    '''    
    A = [1,1]
    B = [N,N]
    A_dir = 3 # 0:down, 1: right, 2: up; 3: left
    B_dir = 1
    while 1:
        # print('meet_or_not: ', A, B)
        A, A_dir = move(A, A_dir)
        B, B_dir = move(B, B_dir)

        if A==B:
            # print('meet_or_not(maze) with {0}: Can meet'.format(maze))
            return True
        #if (A == [1,1]) or (A == [N,N]) or (B == [1,1]) or (B == [N,N]):
        if (A == [N,N]) or (B == [1,1]):            
            break
    # print('meet_or_not(maze) with \n{0}: Cannot meet'.format(maze))
    return False

# # test meet_or_not()
# N = 4
# maze = np.zeros((N+2, N+2))
# maze[1,1] = 1
# maze[1,3] = 1
# maze[2,1:5] = 1
# maze[3,1] = 1
# maze[3,3] = 1
# maze[4,2:5] = 1
# print(maze)
# print(meet_or_not(maze))


tStart  = time.perf_counter()      
N = 5
count = 0
item_cnt = 0
for item in it.product([0,1],repeat=N**2):
    item_cnt += 1
    if item_cnt%100000 == 0:
        print('item_cnt = {0}'.format(item_cnt))
    if item[0]==0 or item[N*N-1]==0:
        # The left-top and right-down corners must not be wall.
        continue
        
    # print(item)
    # Maze initialization
    # Assuming, '0' represents wall; '1' represent passage
    # Add guard for easy judge, and guard is also initialized to '0'
    maze = np.zeros((N+2, N+2))
    for k in range(N):
        for j in range(N):
            maze[k+1,j+1] = item[k*N+j]
            
    # Judge whether this maze is valid
    if not is_valid_maze(maze):
        # Not a valid maze, skip the following processing, go to the next
        # print(maze, 'invalid')
        continue 
    
    # For a valid maze, decide whether A and B can meet
    if meet_or_not(maze):
        count = count + 1
        
tCost  = time.perf_counter() - tStart
print('N={0}, count = {1}, tCost = {2:6.3f}(sec)'.format(N,count,tCost))
        