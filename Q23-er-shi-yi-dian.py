# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 07:56:17 2021

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
    def point21game1(self, coin:int, steps:int)->int:
        """
        Parameters
        ----------
        coin : The money for the start
        steps    : The number of steps of game

        Returns  : The number of paths for which there is money left        
        -------
        """
        k = 0
        count    = 0
        for item in it.product([1,-1],repeat=steps):
            # print(item)
            # k+=1
            # if k%(65536*4) == 0:
            #     print('k = {0}'.format(k//(65536*4)))
            
            balance = 0
            flag = True
            for i in item:                
                balance += i
                if balance == -coin:
                    flag = False
                    break
            if flag:
                count += 1
        return count

    def point21game2(self, coin:int, steps:int)->int:
        """
        Parameters
        ----------
        coin : The money for the start
        steps   : The number of steps of game

        Returns : The number of paths for which there is money left        
        -------
        """
        # path  = []
        # balance  = 0
        def explore(path, balance):
            if len(path)==steps and balance > (-coin):
                return 1
            
            count = 0
            for stake in [1,-1]:
                if (balance + stake) > (-coin):
                    count += explore(path+[stake],balance+stake)
                    
            return count
        
        return explore([],0)

    def point21game3(self, coin:int, steps:int)->int:
        """
        Parameters
        ----------
        coin : The money for the start
        steps    : The number of steps of game

        Returns  : The number of paths for which there is money left        
        -------
        """
        
        memo    = dict()
        def dp(k, c):
            # print('k={0},c={1}'.format(k,c))
            if (k,c) in memo:
                return memo[(k,c)]
            if c == 0:
                return 0
            if k == 0:
                return 1
                                
            return dp(k-1,c+1) + dp(k-1,c-1)
        
        return dp(steps,coin)
        
if __name__ == '__main__':        
            
    sln     = Solution()   
    coin = 1
    steps   = 4
    tStart  = time.perf_counter()
    count1  = sln.point21game1(coin, steps)
    count2  = sln.point21game2(coin, steps)
    count3  = sln.point21game3(coin, steps)
    tCost   = time.perf_counter() - tStart
    print('({0}, {1}), count1 = {2}, tCost = {3:6.3f}(sec)'.format(coin,steps,count1,tCost))        
    print('({0}, {1}), count2 = {2}, tCost = {3:6.3f}(sec)'.format(coin,steps,count2,tCost))        
    print('({0}, {1}), count3 = {2}, tCost = {3:6.3f}(sec)'.format(coin,steps,count3,tCost))        

    coin = 10
    steps    = 24
    tStart = time.perf_counter()
    count1 = sln.point21game1(coin, steps)
    tCost  = time.perf_counter() - tStart
    print('({0}, {1}), count1 = {2}, tCost = {3:6.3f}(sec)'.format(coin,steps,count1,tCost))            

    tStart = time.perf_counter()
    count2 = sln.point21game2(coin, steps)
    tCost  = time.perf_counter() - tStart
    print('({0}, {1}), count2 = {2}, tCost = {3:6.3f}(sec)'.format(coin,steps,count2,tCost))            
    
    tStart = time.perf_counter()
    count3 = sln.point21game3(coin, steps)
    tCost  = time.perf_counter() - tStart
    print('({0}, {1}), count3 = {2}, tCost = {3:6.3f}(sec)'.format(coin,steps,count3,tCost))   