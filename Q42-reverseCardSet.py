# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 09:06:49 2021

@author: chenxy
"""
import sys
import time
import random
from   typing import List
from   queue import Queue
from   collections import deque

class Solution:
    def reverseCardSet0(self, N: int) -> List:
        stateQue = Queue(maxsize = 0) # an infinite queue for storing card set state
        distQue  = Queue(maxsize = 0) # an infinite queue for storing distance of each corresponding state
        
        s_start  = [k for k in range(1,2*N+1)]
        s_end    = [k for k in range(2*N,0,-1)]
        # print('s_start = ', s_start)
        # print('s_end = ', s_end)
        distQue.put(0)
        stateQue.put(s_start)
        visited = []
        
        while not stateQue.empty():
            curState = stateQue.get()
            curDist  = distQue.get()
            visited.append(curState)
            # print('curState: ',curState)
            if curState == s_end:
                return [curDist,len(visited)]
            else:                
                for k in range(1,N+1):
                    childState = curState[k:k+N] + curState[0:k] + curState[k+N:]
                    # print('    childState: ',childState)
                    if childState not in visited:
                        distQue.put(curDist+1)
                        stateQue.put(childState)

    def reverseCardSet1(self, N: int) -> List:
        stateQue = deque() # Using deque is faster than Queue.
        distQue  = deque()
        
        s_start  = [k for k in range(1,2*N+1)]
        s_end    = [k for k in range(2*N,0,-1)]
        # print('s_start = ', s_start)
        # print('s_end = ', s_end)
        distQue.append(0)
        stateQue.append(s_start)
        visited = [s_start]
        
        while len(stateQue) > 0:
            curState = stateQue.popleft()
            curDist  = distQue.popleft()
            # visited.append(curState)
            # print('curState: ',curState)
            if curState == s_end:
                return [curDist,len(visited)]
            else:                
                for k in range(1,N+1):
                    childState = curState[k:k+N] + curState[0:k] + curState[k+N:]
                    # print('    childState: ',childState)
                    if childState not in visited:
                        distQue.append(curDist+1)
                        stateQue.append(childState)
                        visited.append(childState)

    def reverseCardSet2(self, N: int) -> List:
        stateQue = deque() # Using deque is faster than Queue.
        distQue  = deque()
        
        s_start  = tuple([k for k in range(1,2*N+1)])
        s_end    = tuple([k for k in range(2*N,0,-1)])
        # print('s_start = ', s_start)
        # print('s_end = ', s_end)
        distQue.append(0)
        stateQue.append(s_start)
        visited = dict()
        visited[s_start] = ''
        
        while len(stateQue) > 0:
            curState = stateQue.popleft()
            curDist  = distQue.popleft()
            # visited.append(curState)
            # print('curState: ',curState)
            if curState == s_end:
                return [curDist,len(visited)]
            else:                
                for k in range(1,N+1):
                    childState = curState[k:k+N] + curState[0:k] + curState[k+N:]
                    # print('    childState: ',childState)
                    if childState not in visited:
                        distQue.append(curDist+1)
                        stateQue.append(childState)
                        visited[childState] = ''

    # Using list to implement visited(), which is slower than reverseCardSet2() by three orders of magnitude
    def reverseCardSet3(self, N: int) -> List:
        stateQue = deque() # Using deque is faster than Queue.
        distQue  = deque()
        
        s_start  = tuple([k for k in range(1,2*N+1)])
        s_end    = tuple([k for k in range(2*N,0,-1)])
        # print('s_start = ', s_start)
        # print('s_end = ', s_end)
        distQue.append(0)
        stateQue.append(s_start)
        visited = []
        visited.append(s_start)
        
        while len(stateQue) > 0:
            curState = stateQue.popleft()
            curDist  = distQue.popleft()
            # visited.append(curState)
            # print('curState: ',curState)
            if curState == s_end:
                return [curDist,len(visited)]
            else:                
                for k in range(1,N+1):
                    childState = curState[k:k+N] + curState[0:k] + curState[k+N:]
                    # print('    childState: ',childState)
                    if childState not in visited:
                        distQue.append(curDist+1)
                        stateQue.append(childState)
                        visited.append(childState)
                
        
if __name__ == '__main__':        
            
    sln = Solution()

    for N in range(3,6):
        # tStart = time.time()
        # ans = sln.reverseCardSet0(N)
        # tCost = time.time() - tStart
        # print('N = {0}, ans = {1}, tCost = {2}(sec)'.format(N, ans, tCost))                    
        
        # tStart = time.time()
        # ans1 = sln.reverseCardSet1(N)
        # tCost = time.time() - tStart
        # print('N = {0}, ans = {1}, tCost = {2}(sec)'.format(N, ans1, tCost))                            

        tStart = time.time()
        ans2 = sln.reverseCardSet2(N)
        tCost = time.time() - tStart
        print('N = {0}, ans = {1}, tCost = {2}(sec)'.format(N, ans2, tCost))                                          

        # tStart = time.time()
        # ans2 = sln.reverseCardSet3(N)
        # tCost = time.time() - tStart
        # print('N = {0}, ans = {1}, tCost = {2}(sec)'.format(N, ans2, tCost))                                                  
                
                
        