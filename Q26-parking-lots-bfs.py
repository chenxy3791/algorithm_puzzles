# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 07:10:26 2021

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

class Solution:
    def parkingMove(self,N,M):
        
        '''    
        The content stored in Queue:
            [[x1,y1,x2,y2], layer]. (x1,y1): car position; (x2,y2): empty position
        'visited' is implemented as dict() for faster item search, the value is irrelant, hence set to ''.
        (x1,y1,x2,y2) is used as the key of 'visited', instead of [x1,y1,x2,y2], because list is unhashable type.
                
        Returns
        -------
            The number of moves needed to move car to the right-down lot, from top-left lot.
        '''

        def findNext(curState):                        
            nxtStateLst = []
            # empty up
            carPos,emptyPos   = curState[0:2], curState[2:]
            if emptyPos[0] > 0:
                # print('up')
                if carPos[0] == emptyPos[0] - 1 and carPos[1] == emptyPos[1]:                    
                    carPos[0]   = carPos[0] + 1
                emptyPos[0] = emptyPos[0] - 1                    
                nxtStateLst.append(carPos+emptyPos)
            # empty down
            carPos,emptyPos   = curState[0:2], curState[2:]
            if emptyPos[0] < N-1:
                # print('down')
                if carPos[0] == emptyPos[0] + 1 and carPos[1] == emptyPos[1]:                    
                    carPos[0]   = carPos[0] - 1
                emptyPos[0] = emptyPos[0] + 1      
                nxtStateLst.append(carPos+emptyPos)                          
            # empty left
            carPos,emptyPos   = curState[0:2], curState[2:]
            if emptyPos[1] > 0:
                # print('left')
                if carPos[1] == emptyPos[1] - 1 and carPos[0] == emptyPos[0]:                    
                    carPos[1]   = carPos[1] + 1
                emptyPos[1] = emptyPos[1] - 1                                
                nxtStateLst.append(carPos+emptyPos)
            # empty right
            carPos,emptyPos   = curState[0:2], curState[2:]
            if emptyPos[1] < M-1:
                # print('right')
                if carPos[1] == emptyPos[1] + 1 and carPos[0] == emptyPos[0]:                    
                    carPos[1]   = carPos[1] - 1
                emptyPos[1] = emptyPos[1] + 1      
                nxtStateLst.append(carPos+emptyPos)                                      
            # print('findNext: ',curState,' -> ',nxtStateLst)                
            return nxtStateLst
        
        # Initialization
        q = deque()
        visited = dict()
        car_start, empty_start = [0,0], [N-1,M-1]
        car_target = [N-1,M-1]
        
        q.append([car_start + empty_start, 0])
        visited[tuple(car_start + empty_start)] = ''
    
        while len(q) != 0:
            node = q.popleft()            
            # print(node)
            car_pos = node[0][0:2]
            layer   = node[1]
            if car_pos == car_target:
                return layer
            
            nxtStateLst = findNext(node[0])
            for nxtState in nxtStateLst:
                if tuple(nxtState) not in visited:
                    visited[tuple(nxtState)] = ''
                    q.append([nxtState, layer+1])
                            
    
if __name__ == '__main__':      

    sln     = Solution()   
    tStart  = time.perf_counter()
    N,M     = 10,10 # N*M parking-lots
    numOfMoves = sln.parkingMove(N,M)
    tCost   = time.perf_counter() - tStart
    print('N,M={0},{1}, num-of-moves = {2}, tCost = {3:6.3f}(sec)'.format(N,M,numOfMoves,tCost))
    