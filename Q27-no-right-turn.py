# -*- coding: utf-8 -*-
"""

"""
import sys
import time
import random
from   typing import List
# from   queue import Queue

class Solution:
    def NoRightTurn(self, m:int, n:int)->int:
        """
        :m:    number of column (horizontal width) of the rectangular grid network
        :n:    number of row (vertical height) of the rectangular grid network
        :    
        :ret:  the number of the total valid path
        """

        # Initialization
        start   = (1,0)
        target  = (m,n)
        visited = [{(0,0),(1,0)}]
        preMove = 3
        
        def core(start, prevMove, visited)->int:
            """
            :target:   A tuple (x,y) to represent the coordinate of start point
            :prevMove: The previous move. 0: up; 1: left; 2:down; 3: right
            :visited:  A list to hold already-visited edges to avoid repeated visit           
            :          Each edge is represented by a set of tuple:{(x0,y0),(x1,y1)}.
            :ret:      The number of the total valid path
            """
            # print('core: ', start, prevMove, visited)
            if start == target:
                # print('\tcore({0}, {1}, {2} = 1'.format(start,prevMove,visited))
                return 1 # Found one valid path

            num = 0
            for k in range(2):
                newMove  = (prevMove + k)%4
                x = start[0]
                if newMove == 1:
                    x = x - 1
                elif newMove == 3:    
                    x = x + 1

                y = start[1]
                if newMove == 0:
                    y = y + 1
                elif newMove == 2:    
                    y = y - 1                

                # print('\tk={0}, x={1}, y={2}'.format(k,x,y))
                if (x >= 0 and x <= m) and (y >= 0 and y <= n):
                    newStart = (x,y)
                    edge     = set([start,newStart])
                    # print(edge)
                    if edge not in visited:
                        newVisited = visited + [edge]
                        num = num + core(newStart, newMove, newVisited)
            # print('\tcore({0}, {1}, {2} = {3}'.format(start,prevMove,visited,num))
            return num
    
        return core(start,preMove,visited)        
    
if __name__ == '__main__':        
    
    sln = Solution()

    # m,n = 1,1    
    # print('m = {0}, n = {1}, numPath = {2}'.format(m,n,sln.NoRightTurn(m,n)))

    # m,n = 1,2    
    # print('m = {0}, n = {1}, numPath = {2}'.format(m,n,sln.NoRightTurn(m,n)))    

    # m,n = 2,1    
    # print('m = {0}, n = {1}, numPath = {2}'.format(m,n,sln.NoRightTurn(m,n)))        

    m,n = 2,2    
    tStart = time.time()
    num = sln.NoRightTurn(m,n)
    tCost = time.time() - tStart
    print('m = {0}, n = {1}, numPath = {2}, tCost = {3}(sec)'.format(m,n,num,tCost))        

    m,n = 3,2   
    tStart = time.time()
    num = sln.NoRightTurn(m,n)
    tCost = time.time() - tStart
    print('m = {0}, n = {1}, numPath = {2}, tCost = {3}(sec)'.format(m,n,num,tCost))        

    m,n = 4,4    
    tStart = time.time()
    num = sln.NoRightTurn(m,n)
    tCost = time.time() - tStart
    print('m = {0}, n = {1}, numPath = {2}, tCost = {3}(sec)'.format(m,n,num,tCost)) 

    m,n = 5,4    
    tStart = time.time()
    num = sln.NoRightTurn(m,n)
    tCost = time.time() - tStart
    print('m = {0}, n = {1}, numPath = {2}, tCost = {3}(sec)'.format(m,n,num,tCost)) 

    m,n = 6,4    
    tStart = time.time()
    num = sln.NoRightTurn(m,n)
    tCost = time.time() - tStart
    print('m = {0}, n = {1}, numPath = {2}, tCost = {3}(sec)'.format(m,n,num,tCost))       
    
    m,n = 6,6
    tStart = time.time()
    num = sln.NoRightTurn(m,n)
    tCost = time.time() - tStart
    print('m = {0}, n = {1}, numPath = {2}, tCost = {3}(sec)'.format(m,n,num,tCost))    