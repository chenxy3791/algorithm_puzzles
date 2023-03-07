# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:39:27 2021

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

class Solution:
    def stringEquation(self, strEqu:str):
        """
        strEqu: Equation in the form of string with character representing digit, 
                assuming case insensitive.
                Also it is assumed that only integer division is considered
        :ret: The total number of IP satisfying the requirement
        """                
        # Step1: extract the alphabeta characters from the string equation    
        s = strEqu.upper() # Transfer to all uppercase for the convenience of processing        
        cLst = []
        for k in range(len(s)):            
            if s[k].isalpha() and s[k] not in cLst:
                cLst.append(s[k])
            if s[k] == '=':
                equalSignIndex = k
        # print(cLst)
                
        nums = 0
        mapping = []
        for p in it.permutations([k for k in range(10)], len(cLst)): 
            # print(p)
            # Substitute c<->digit mapping back to the input string equation
            # left-hand-side expression, before '='            
            lhs = s[0:equalSignIndex]
            for k in range(len(cLst)):
                lhs = lhs.replace(cLst[k], str(p[k]))
                
            # right-hand-side expression, after '='
            rhs = s[equalSignIndex+1:]
            for k in range(len(cLst)):
                rhs = rhs.replace(cLst[k], str(p[k]))                
            
            # print(lhs, rhs)
            if len(rhs) > 1 and rhs[0] == '0' : # The first digit must be non-zero in multi-digit case
                # print('1')
                continue
            if len(lhs) > 1 and lhs[0] == '0' and lhs[1].isdigit():
                # print('2')
                continue
            if not lhs[-1].isdigit():
                # print('3', lhs, lhs[-1].isdigit() )
                continue
                        
            lhs_valid = True
            for k in range(len(lhs)-2):
                if (not lhs[k].isdigit()) and lhs[k+1]=='0' and lhs[k+2].isdigit():
                    # print('invalid lhs:', lhs)
                    lhs_valid = False
                    break
            if not lhs_valid:
                continue
            
            # print('valid:', lhs, rhs, eval(lhs), eval(rhs))
            if eval(lhs) == eval(rhs):
                nums = nums + 1
                mapping.append((cLst,p,lhs+'='+rhs))
        
        return nums, mapping
                    
if __name__ == '__main__':        
            
    sln    = Solution()            

    tStart = time.time()
    strEqu = 'A*B=C'
    nums, mapping = sln.stringEquation(strEqu)
    tCost  = time.time() - tStart
    print('nums={0}, tCost = {1:6.3f}(sec)'.format(nums,tCost))   
    for item in mapping:
        print('\t',item)
    
    tStart = time.time()
    strEqu = 'We*love=CodeIQ'
    nums, mapping = sln.stringEquation(strEqu)
    tCost  = time.time() - tStart
    print('nums={0}, tCost = {1:6.3f}(sec)'.format(nums,tCost))    
    for item in mapping:
        print('\t',item)
    
    tStart = time.time()
    strEqu = 'READ+WRITE+TALK=SKILL'
    nums, mapping = sln.stringEquation(strEqu)
    tCost  = time.time() - tStart
    print('nums={0}, tCost = {1:6.3f}(sec)'.format(nums,tCost))        
    for item in mapping:
        print('\t',item)    