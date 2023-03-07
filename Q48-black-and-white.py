# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 07:40:08 2021

@author: chenxy
"""

# import sys
import time
# import datetime
# import math
# import random
# from   typing import List
# from   queue import Queue
from   collections import deque
# import itertools as it
# import numpy as np

N       = 8
target1 = 0b1010_1010_1010_1010
target2 = 0b0101_0101_0101_0101
start   = 0b0000_0000_1111_1111

mask    = 2*N*[0]
for k in range(2*N):
    mask[k] = (7 << k) // (2**16) + (7 << k) % (2**16)

step    = 0
q       = deque()
visited = set()

q.append((start,step))
visited.add(start)

while len(q) > 0:
    cur,step = q.popleft()
    # print('cur={0}, step={1}'.format(cur,step))
    if cur == target1 or cur == target2:
        break
    for k in range(2*N):
        nxt = cur ^ mask[k]
        if nxt not in visited:
            # print('\t{0}-->{1}'.format(cur,nxt))
            q.append((nxt,step+1))
            visited.add(nxt)

print('N = {0}, step = {1}'.format(N,step))