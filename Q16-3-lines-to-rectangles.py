# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 08:32:06 2021

@author: chenxy
"""

import sys
import time
import random
from math import gcd, sqrt, ceil
from   typing import List
# from   queue import Queue

class Solution:

    def lines2rectangles1(self, L:int)->int:
        """
        :L:    The length of the lines
        :    
        :ret:  The number of the solutions
        """
        aMax = L // 4
        
        valid_cnt = 0
        for a in range(1,aMax+1):
            for x1 in range(1,ceil(a/sqrt(2))): # Assuming that x1 <= x2 < a, without loss of generality
                for x2 in range(x1,a): 
                    if x1*(2*a-x1) + x2*(2*a-x2) == a*a:
                        if gcd(a,x1) == 1: # gcd(a,x1) --> gcd(a,x1,x2)
                            valid_cnt = valid_cnt + 1
                            # print('a = {0}, x1 = {1}, x2 = {2}'.format(a,x1,x2))        
        
        return valid_cnt

    def lines2rectangles2(self, L:int)->int:
        """
        :L:    The length of the lines
        :    
        :ret:  The number of the solutions
        """
        aMax = L // 4
        
        valid_cnt = 0
        for a in range(1,aMax+1): # Assuming that x1 <= x2 < a, without loss of generality
            a_squ = a*a
            for x1 in range(1,ceil(a/sqrt(2))):
                area1 = x1*(2*a-x1)
                area2 = a_squ - area1
                for x2 in range(x1,a):
                    if x2*(2*a-x2) == area2:
                        if gcd(a,x1) == 1: # gcd(a,x1) --> gcd(a,x1,x2)
                            valid_cnt = valid_cnt + 1
                            # print('a = {0}, x1 = {1}, x2 = {2}'.format(a,x1,x2))                
        return valid_cnt
    
    def lines2rectangles3(self, L:int)->int:
        """
        :L:    The length of the lines
        :    
        :ret:  The number of the solutions
        """
        aMax = L // 4
        
        valid_cnt = 0
        for a in range(1,aMax+1): # Assuming that x1 <= x2 < a, without loss of generality
            a_squ = a*a
            for x1 in range(1,ceil(a/sqrt(2))):
                if gcd(a,x1) == 1: # gcd(a,x1) --> gcd(a,x1,x2)
                    area1 = x1*(2*a-x1)
                    area2 = a_squ - area1
                    for x2 in range(x1,a):
                        if x2*(2*a-x2) == area2:                    
                            valid_cnt = valid_cnt + 1
                            # print('a = {0}, x1 = {1}, x2 = {2}'.format(a,x1,x2))                                            
        return valid_cnt
                
    def lines2rectangles4(self, L:int)->int:
        """
        :L:    The length of the lines
        :    
        :ret:  The number of the solutions
        """
        aMax = L // 4
        
        valid_cnt = 0
        for a in range(1,aMax+1): # Assuming that x1 <= x2 < a, without loss of generality
            a_squ = a*a
            for x1 in range(1,ceil(a/sqrt(2))):
                if gcd(a,x1) == 1: # gcd(a,x1) --> gcd(a,x1,x2)                    
                    diff = a_squ - x1*x1
                    for x2 in range(ceil(a/sqrt(2)),a):
                        if x2*x2 == diff:                    
                            valid_cnt = valid_cnt + 1
                            # print('a = {0}, x1 = {1}, x2 = {2}'.format(a,x1,x2))                                            
        return valid_cnt
        
if __name__ == '__main__':        
    
    sln = Solution()

    L = 20
    tStart = time.time()
    num = sln.lines2rectangles1(L)
    tCost = time.time() - tStart
    print('L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))        

    L = 500
    tStart = time.time()
    num = sln.lines2rectangles1(L)
    tCost = time.time() - tStart
    print('#1: L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))        
    tStart = time.time()
    num = sln.lines2rectangles2(L)
    tCost = time.time() - tStart    
    print('#2: L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))        
    
    L = 2000
    tStart = time.time()
    num = sln.lines2rectangles1(L)
    tCost = time.time() - tStart
    print('#1: L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))        
    tStart = time.time()
    num = sln.lines2rectangles2(L)
    tCost = time.time() - tStart
    print('#2: L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))     
    tStart = time.time()
    num = sln.lines2rectangles3(L)
    tCost = time.time() - tStart
    print('#3: L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))         
    tStart = time.time()
    num = sln.lines2rectangles4(L)
    tCost = time.time() - tStart
    print('#4: L = {0}, numSlns = {1}, tCost = {2}(sec)'.format(L,num,tCost))             