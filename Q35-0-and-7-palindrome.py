# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:12:48 2021

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
from   math import sqrt, floor, ceil
import numpy as np

def palindrome(k:int)->bool:
    k_decstr = str(k)
    return k_decstr == k_decstr[::-1]

check_list = list(range(1,51,2))
ok_dict    = dict()
ng_dict    = dict()
t1 = time.perf_counter()

m = 1 # 'm': set the number of digits   
while 1:
    aSet = set() # Use set to remove repetition
    for item in it.product(['0','7'], repeat=m):
        # print(item)
        if item[0]=='0' or ('0' not in item):
        # if item[0]=='0':    
            continue
        
        # print(''.join(list(each)))
        aDec = int(''.join(list(item)))
        for k in check_list:
            if k in ok_dict or k in ng_dict:
                continue
            if aDec % k == 0:
                if palindrome(aDec):
                    ok_dict[k] = (aDec//k,aDec)
                else:
                    ng_dict[k] = (aDec//k,aDec)
    if len(ok_dict)+len(ng_dict) == len(check_list):
        break
    m = m+1
    
tCost = time.perf_counter() - t1
print('Number of ok_dict = {0}, tCost = {1:6.3f}'.format(len(ok_dict),tCost))            
for key in ok_dict:
    print('\t',key, ok_dict[key])
                

# # Brute-Force
# def check_0_7(k)->bool:
#     k_str = str(k)
#     return set(k_str) == {'0','7'}
#     # return set(k_str).issubset({'0','7'})

# ans = []
# t1 = time.perf_counter()
# ok_dict    = dict()
# ng_dict    = dict()
# for n in range(1,50,2):    
#     if n%5==0:
#         continue
#     # print(n)        
#     m = 1
#     while 1: 
#         k = m*n
#         # print(n,m,k)        
#         if check_0_7(k):
#             # print(n,m,k)        
#             if palindrome(k):
#                 ok_dict[n] = (m,k)
#             else:
#                 ng_dict[n] = (m,k)
#             break
#         m += 1
    
# tCost = time.perf_counter() - t1      
# print('Number of ok_dict = {0}, tCost = {1}'.format(len(ok_dict),tCost))            
# for key in ok_dict:
#     print('\t',key, ok_dict[key])



    
    