# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 08:23:21 2021

@author: chenxy
"""

import sys
import time
import datetime
import random
from   typing import List
from   collections import deque
import itertools as it
import numpy as np

# all_white = int('0000000000000000',2)
mask_lut = dict()
mask_lut[ 0] = 0b1111_1000_1000_1000
mask_lut[ 1] = 0b1111_0100_0100_0100
mask_lut[ 2] = 0b1111_0010_0010_0010
mask_lut[ 3] = 0b1111_0001_0001_0001
mask_lut[ 4] = 0b1000_1111_1000_1000
mask_lut[ 5] = 0b0100_1111_0100_0100
mask_lut[ 6] = 0b0010_1111_0010_0010
mask_lut[ 7] = 0b0001_1111_0001_0001
mask_lut[ 8] = 0b1000_1000_1111_1000
mask_lut[ 9] = 0b0100_0100_1111_0100
mask_lut[10] = 0b0010_0010_1111_0010
mask_lut[11] = 0b0001_0001_1111_0001
mask_lut[12] = 0b1000_1000_1000_1111
mask_lut[13] = 0b0100_0100_0100_1111
mask_lut[14] = 0b0010_0010_0010_1111
mask_lut[15] = 0b0001_0001_0001_1111

all_white = 0b0000_0000_0000_0000
visited   = set()
q         = deque()
q.append((all_white,0))
visited.add(all_white)

tStart  = time.perf_counter()
while len(q) > 0:
    board, layer = q.popleft()
    for k in range(16):
        mask = mask_lut[k]
        nxt_board = mask ^ board
        if nxt_board not in visited:
            visited.add(nxt_board)
            q.append((nxt_board,layer+1))
            
tCost  = time.perf_counter() - tStart

print('final_board = {0}, layer = {1}, tCost = {2:6.3f}(sec)'.format(board,layer,tCost))  
        