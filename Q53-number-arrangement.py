# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 12:43:46 2021

@author: chenxy
"""
import sys
import time
# import random
# from   typing import List
# from   queue import Queue
# from   collections import deque

class Solution:
    def numberArrangement(self, N: int) -> int:
        """
        :N:    
        :ret:  The number of arrangement
        """        
        start   = 2*N*[0]    # Nested list to represent state/node
                                            
        def explore(curState, num):
            """
            :curState: current state to explore
            :num:     the number to be arranged
            :ret:     the number of arrangements
            """
            # print('explore({0}, {1})'.format(curState, num))
            # Judge whether reach the goal or final state.
            if num > N:
                return 1
            
            sum = 0
            for k in range(0,2*N-num-1):
                if curState[k]==0 and curState[k+num+1]==0:
                    # nxtState    = curState # Both points to the same object! NG
                    nxtState    = curState.copy()
                    nxtState[k] = num
                    nxtState[k+num+1] = num
                    sum += explore(nxtState,num+1)            
            return sum

        return explore(start,1)
                
if __name__ == '__main__':        
            
    sln = Solution()    

    for N in range(2,12):
        tStart = time.time()
        ans    = sln.numberArrangement(N)
        tCost  = time.time() - tStart
        print('N={0}, ans = {1}, tCost = {2}(sec)'.format(N,ans,tCost))        