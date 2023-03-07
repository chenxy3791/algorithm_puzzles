# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:54:43 2021

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

maxNumCross = 0
maxPath     = []

def isCross(edge1, edge2)->int:
    """
    Judge whether two edges cross

    Parameters
    ----------
    edge1 : tuple, (x,y)
        x represents the line number in left column
        y represents the line number in righg column
    edge2 : Same as edge1

    Returns: int. 0: not cross, 1: cross
    -------
    """
    if (edge1[0] - edge2[0]) * (edge1[1] - edge2[1]) < 0:
        return 1
    else:
        return 0

def explore(left:List, right:List, activeCol:int, lastPole:int, pathHist:List)->int:
    """
    Explore the total number of paths under the condition of "left" and "right", which
    contains the left poles in the left and right column, repectively.
    
    Parameters
    ----------
    left :  List. The left poles in the left column        
    right : List. The left poles in the right column                
    activeCol: int, indicate which column should be used in the next step. 0: left, 1, right
    Returns
    -------
    int:    The total number of paths traversing all the poles in interleaving way.
    """
    global maxNumCross
    global maxPath
    if len(left)==0 and len(right)==0:
        # find one path, and count the number of crosses
        # Firstly, add the last edge from lastPole to the first pole of right pole
        pathHist.append([lastPole,0])        
        numCross = 0
        for edges in it.combinations(pathHist, 2):
            edge1 = edges[0]
            edge2 = edges[1]
            numCross += isCross(edge1,edge2)        
        if numCross > maxNumCross:
            maxNumCross = numCross
            maxPath = pathHist.copy()
        pathHist.remove([lastPole,0])
        return 1
    
    count = 0
    if activeCol == 0:
        nxtActiveCol = 1
        for pole in left:
            nxtLeft = left.copy()
            nxtLeft.remove(pole)
            pathHist.append([pole,lastPole])
            count += explore(nxtLeft,right,nxtActiveCol,pole,pathHist)
            pathHist.remove([pole,lastPole])
    else:
        nxtActiveCol = 0
        for pole in right:
            nxtRight = right.copy()
            nxtRight.remove(pole)
            pathHist.append([lastPole,pole])
            count += explore(left,nxtRight,nxtActiveCol,pole,pathHist)        
            pathHist.remove([lastPole,pole])
            
    return count

if __name__ == '__main__':        
    
    # tStart  = time.perf_counter()
    # print(explore([1],[1],1,0,[]))            
    # tCost   = time.perf_counter() - tStart
    # print('Number of cross = {0}, tCost = {1:6.3f}(sec)'.format(maxNumCross, tCost))
    # print(maxPath)
    
    tStart  = time.perf_counter()
    print(explore([1,2,3,4,5],[1,2,3,4,5],1,0,[]))            
    tCost   = time.perf_counter() - tStart
    print('Number of cross = {0}, tCost = {1:6.3f}(sec)'.format(maxNumCross, tCost))
    print(maxPath)