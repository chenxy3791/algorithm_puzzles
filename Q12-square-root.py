# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:51:51 2021

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

class Solution:
    def squareRoot1(self, sel:int) -> tuple:
        """
        Find the first interger, for which, either the first 10 digits of its square root, 
        or the first 10 digits of the decimal part of its square root, 
        includes all of 0~9.        
        sel:  0--including integer part; 1: not including integer part
        :ret: 
        """                
        i = 1
        while(1):
            i_sqrt = math.sqrt(i)
            i_sqrt_str = str(i_sqrt)

            # Find the position of decimal point
            for k in range(len(i_sqrt_str)):
                if i_sqrt_str[k] == '.':
                    break            
                
            if sel == 0:
                first10 = i_sqrt_str[0:k] + i_sqrt_str[k+1:11]
            else:
                first10 = i_sqrt_str[k+1:k+11]
                # print(first10,list(first10),set(list(first10)))
            
            if len(set(list(first10))) == 10:
                return i, i_sqrt
            
            i = i+1

    def squareRoot2(self) -> tuple:
        '''
        Find the first interger, for which, the first 10 digits of the decimal part of its square root, 
        includes all of 0~9.        
        :ret: 
        '''
        num=1
        str_num='1.000000000000000'
        while len(set(list(str_num.split('.')[1][:10])))!=10:
        	num+=1
        	str_num=str(num**0.5)
        return num, num**0.5
                    
if __name__ == '__main__':        
            
    sln    = Solution()            
    
    tStart = time.time()
    num1,num1_sqrt = sln.squareRoot1(0) # including integer part
    num2,num2_sqrt = sln.squareRoot1(1) # Only considering fractional part
    tCost  = time.time() - tStart
    print('num1={0}, num1_sqrt={1:.10f}, tCost = {2:6.3f}(sec)'.format(num1,num1_sqrt,tCost))    
    print('num2={0}, num2_sqrt={1:.10f}, tCost = {2:6.3f}(sec)'.format(num2,num2_sqrt,tCost))    

    tStart = time.time()
    num3,num3_sqrt = sln.squareRoot2() # Only considering fractional part    
    tCost  = time.time() - tStart
    print('num3={0}, num3_sqrt={1:.10f}, tCost = {2:6.3f}(sec)'.format(num3,num3_sqrt,tCost))        