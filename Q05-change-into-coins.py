# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:35:32 2021

@author: chenxy
"""

import sys
import time
import random
from math import gcd, sqrt, ceil
from   typing import List
# from   queue import Queue

class Solution:

    def coinChange(self, money:int, coins:List, maxNum: int)->int:
        """
        :money:  The money value to be changed into coins
        :coins:  Candiate coins in decreasing value order
        :    
        :ret:    The number of the solutions
        """
        # print('money={0}, coins={1}, maxNum={2}'.format(money,coins,maxNum))
        # Boundary cases
        if money == 0:
            return 1
        
        if len(coins) == 0:
            return 0
        
        # If money is less than the smallest coin, then the change is unsuccessful
        if money < coins[-1]:
            return 0
        
        # Cannot be changed into no larger than maxNum coins
        if ceil(money/coins[0]) > maxNum:
            return 0
        
        nums = 0
        for k in range(money//coins[0]+1):
            nums += self.coinChange(money-k*coins[0], coins[1:], maxNum-k)
            
        return nums
                
if __name__ == '__main__':        
    
    sln = Solution()

    money = 1000
    coins = [500,100,50,10] # In decreasing value order
    maxNum= 15
    tStart = time.time()
    nums = sln.coinChange(money, coins, maxNum)
    tCost = time.time() - tStart
    print('money = {0}, coins = {1}, nums = {2}, tCost = {3}(sec)'.format(money,coins,nums,tCost))             