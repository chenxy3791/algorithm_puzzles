# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 08:23:28 2021

@author: chenxy
"""

import sys
import time
import random
# from math import gcd, sqrt, ceil
# from   typing import List
# from   queue import Queue

class Solution:

    def shortestRoundTrip(self, N:int)->int:
        """
        :N:    The size of the square grid network
        :    
        :ret:  The number of the solutions
        """

        leftBotm  = (0,0)        
        rightTop  = (N,N)        
        
        def dfs(edge, pathCnt, visited):
            # print('dfs: edge = ',edge)
            if edge[1] == leftBotm: # Complete one round-trip
                # print('dfs: Complete one round-trip!')
                return pathCnt + 1                
            
            visited.append(edge)
            visited.append((edge[1],edge[0],1-edge[2]))
            
            # Decide the candidates for the next edge. Care for not crossing the boundary
            x = edge[1][0]
            y = edge[1][1]            
            if edge[2] == 0: # Forward path
                if x == N and y == N: #edge[1] == rightTop: 
                    nxtedge1 = (edge[1],(x-1,y),1)  # Move left
                    nxtedge2 = (edge[1],(x,y-1),1)  # Move down                  
                elif x == N:
                    nxtedge1 = ()
                    nxtedge2 = (edge[1],(x,y+1),0)  # Move up
                elif y == N:
                    nxtedge2 = ()
                    nxtedge1 = (edge[1],(x+1,y),0)  # Move right
                else:
                    nxtedge1 = (edge[1],(x+1,y),0)  # Move right
                    nxtedge2 = (edge[1],(x,y+1),0)  # Move up                    
            else:
                if x == 0:
                    nxtedge1 = ()
                    nxtedge2 = (edge[1],(x,y-1),1)  # Move down                                      
                elif y == 0:
                    nxtedge2 = ()
                    nxtedge1 = (edge[1],(x-1,y),1)  # Move left
                else:
                    nxtedge1 = (edge[1],(x-1,y),1)  # Move left
                    nxtedge2 = (edge[1],(x,y-1),1)  # Move down                                      
                    
            pathCnt1,pathCnt2 = 0,0
            if (nxtedge1 not in visited) and (nxtedge1 != ()):
                pathCnt1 = dfs(nxtedge1,pathCnt,visited)
            if (nxtedge2 not in visited) and (nxtedge2 != ()):
                pathCnt2 = dfs(nxtedge2,pathCnt,visited)
            
            visited.pop()
            visited.pop()
            
            return pathCnt1 + pathCnt2
             
        # Start from the following two call, and finally return pathCnt
        return dfs(((0,0),(0,1),0),0,[]) + dfs(((0,0),(1,0),0),0,[])
        
if __name__ == '__main__':        
    
    sln = Solution()

    for N in range(2,8):
        tStart = time.time()
        num = sln.shortestRoundTrip(N)
        tCost = time.time() - tStart
        print('N = {0}, numSlns = {1}, tCost = {2}(sec)'.format(N,num,tCost))      
    