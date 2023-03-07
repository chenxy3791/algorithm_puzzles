# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:31:11 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
import numpy as np

def baseM_toGray(M: int, N: int, value: int) -> List:
    ''' 
    Parameters
    ----------
    M : int. Base        
    N : int. Number of digits
    value : int. Natural decimal value of the input data

    Returns
    -------
    List
        The base-M gray code representation. 
        [0]: The most siginificant digit
        [-1]: The least siginificant digit
    '''
    # Generate the normal base-M representation of value
    baseM = N * [0]
    for i in range(N-1,-1,-1):
        baseM[i] = value % M
        value    = value //M
    
	# Convert the normal baseM number into the Gray code equivalent. 
    # Note that, the loop starts at the most significant digit and goes down.
    gray  = N * [0]
    shift = 0
    i     = 0
    while i <= N-1:
		# The Gray digit gets shifted down by the sum of the higher digits.
        gray[i] = (baseM[i] + shift) % M
        shift   = shift + M - gray[i];	# Subtract from base so shift is positive      
        i       = i + 1
    return gray      

def cyclicSteps(M: int, N: int, start: int)->int:
    
    cur = start
    step  = 0
    while 1:
        step = step + 1
        curGray = baseM_toGray(M,N,cur)
        # print(curGray)
    
        # Take curGray as normal baseM representation and calulate its value
        cur   = 0
        scale = 1        
        for k in range(N-1,-1,-1):            
            cur = cur + curGray[k] * scale
            scale = scale * M
        if cur == start:
            break
    return step
        
if __name__ == '__main__':           
    
    M = 16
    N = 6
    start = 0x808080
    step  = cyclicSteps(M,N,start)
    print('start = 0x{0:6x}, step = {1}'.format(start,step))
    start = 0xABCDEF
    step  = cyclicSteps(M,N,start)
    print('start = 0x{0:6x}, step = {1}'.format(start,step))