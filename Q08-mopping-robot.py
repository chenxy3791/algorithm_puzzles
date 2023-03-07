# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:30:34 2021

@author: chenxy
"""

import sys
import time
import datetime
# import random
from   typing import List
# from   queue import Queue
# from   collections import deque

class Solution:
    def mopRobot(self, N: int) -> int:
        """
        :N:   The total number of steps
        :ret: The total number of moving paths
        """                
        
        def explore(pathHistory, numSteps):
            # Baseline case: numSteps = 0 means the move is finished.
            if numSteps == 0:
                return 1
            
            # Explore the four directions to search the allowed move
            sum    = 0
            # up move
            curPos    = pathHistory[-1]
            nxtPos    = tuple([curPos[0], curPos[1] + 1])
            if nxtPos not in pathHistory:
                sum += explore(pathHistory + [nxtPos], numSteps-1)
                
            # down move
            curPos    = pathHistory[-1]
            nxtPos    = tuple([curPos[0], curPos[1] - 1])
            if nxtPos not in pathHistory:
                sum += explore(pathHistory + [nxtPos], numSteps-1)                
                
            # left move
            curPos    = pathHistory[-1]
            nxtPos    = tuple([curPos[0] - 1, curPos[1]])
            if nxtPos not in pathHistory:
                sum += explore(pathHistory + [nxtPos], numSteps-1)                                

            # right move
            curPos    = pathHistory[-1]
            nxtPos    = tuple([curPos[0] + 1, curPos[1]])
            if nxtPos not in pathHistory:
                sum += explore(pathHistory + [nxtPos], numSteps-1)                                                
                
            return sum

        return explore([(0,0)],N)        
    
if __name__ == '__main__':        
            
    sln    = Solution()    

    for N in range(2,15,2):
        tStart = time.time()
        ans    = sln.mopRobot(N)
        tCost  = time.time() - tStart
        print('N={0}, ans={1}, tCost = {2:.3f}(sec)'.format(N,ans,tCost))        
        