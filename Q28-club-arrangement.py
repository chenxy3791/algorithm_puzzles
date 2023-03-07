# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:03:13 2021

@author: chenxy
"""

import sys
import time
# import random
# from   typing import List
# from   queue import Queue
# from   collections import deque

class Solution:
    def maxValueRecursion(self, values, costs, maxCost) -> int:
        """
        :values:  The area required by each club, assuming [0] is a dummy placeholder
        :costs:   Number of people in each club, assuming [0] is a dummy placeholder
        :maxHumans: The maximum number of people allowed
        :ret:    The maximum area needed
        """        
        
        memo = dict()
        
        def V(i,j):
            """
            i:   Up to the i-th club (1,2,...,i) are taken into consideration
            j:   Maximum allowed number of people
            ret: The maximum area required
            """
            # Baseline case
            if j <= 0 or i <= 0:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            # Recursive equation
            if costs[i] <= j:
                tmp = max(V(i-1,j), values[i] + V(i-1,j-costs[i]))
            else:
                tmp = V(i-1,j)
            memo[(i,j)] = tmp
            # print('V({0},{1}) = {2}'.format(i,j,tmp))            
            return tmp
            
        return V(len(values)-1,maxCost)
    
        
if __name__ == '__main__':        
            
    sln = Solution()    

    tStart = time.time()
    areas  = [0, 11000, 8000, 400, 800, 900, 1800, 1000, 7000, 100, 300]
    humans = [0, 40, 30, 24, 20, 14, 16, 15, 40, 10, 12]
    maxHumans = 150
    ans = sln.maxValueRecursion(areas, humans, maxHumans)
    tCost = time.time() - tStart
    print('areas = {0}'.format(areas))
    print('humans = {0}'.format(humans))
    print('maxHumans = {0}, maxArea = {1}, tCost = {2}(sec)'.format(maxHumans, ans, tCost))