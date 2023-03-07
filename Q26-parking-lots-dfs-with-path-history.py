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
# from   collections import deque
import itertools as it

minSteps = 1024
movePath = None
class Solution:
    def parkingMove(self,N,M):
        
        # memo = dict()

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
            
    
        def explore(stateHist, numSteps)->int:
            '''    
            Parameters
            ----------
            stateHist : List
                Store the path history, each element has the format of [x1,y1,x2,y2]. 
                x1,y1: car position; x2,y2: empty position; 
                # Dictionary to store the path history. Using dict instead of list is for the 
                # efficiency of search.
            # lastStep : List of tuples, indicated the position of car and empty, respectively
                # [(x1,y1),(x2,y2)]. (x1,y1): car position; (x2,y2): empty position; 
            numSteps : int
                The accumulated steps of the current path.
        
            Returns
            -------
                The number of paths
            '''
            # print('explore: ',stateHist, numSteps)
            global minSteps, movePath
            
            if stateHist[-1][:2] == [N-1,M-1]: # Car is in the target pos
                if minSteps > numSteps:
                    minSteps = numSteps
                    movePath = stateHist
                return 1
        
            # if stateHist in memo:
                # return memo[]
            
            count = 0
            # Traverse all the valid next states:
            nxtStateLst = findNext(stateHist[-1])
            for nxtState in nxtStateLst:
                if nxtState not in stateHist:
                    count += explore(stateHist+[nxtState], numSteps+1)
            return count
        
        return explore([[0,0,N-1,M-1]],0)

if __name__ == '__main__':      

    sln     = Solution()   
    tStart  = time.perf_counter()
    N,M     = 3,3 # N*M parking-lots
    print('N,M={0},{1}, num-of-move-paths = {2}'.format(N,M,sln.parkingMove(N,M)))            
    tCost   = time.perf_counter() - tStart
    print('minSteps = {0}, tCost = {1:6.3f}(sec)'.format(minSteps, tCost))
    print('movePath = {0}'.format(movePath))    
    
    
    