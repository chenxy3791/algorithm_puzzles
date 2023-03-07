# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 07:14:15 2021

@author: chenxy
"""

import sys
import time
import datetime
# import random
from   typing import List
# from   queue import Queue
# from   collections import deque

class Solution:
    
    def noEqualPartition(self, M:int, F:int) -> int:
        """
        :M:     The number of boys
        :F:     The number of girls
        :ret:   The number of incoming order for no-equal-partition.
        """               
                
        memo = dict()
        # Recursion core: 
        # Return the number of incoming orders which would satisfy the condition, 
        # when the number of already arrived boys and girls are m and f respectively
        def recursion(m,f):        
            # print('m,f=',m,f)

            if (m,f) in memo:
                return memo[(m,f)]
                
            if (m==f) and m>0:
                memo[(m,f)] = 0
                return 0
            if (M-m)==(F-f) and (M-m)>0 : # Found equal partition
                memo[(m,f)] = 0
                return 0
            if (M==m and f>=m) or (F==f and (m>=f)):
                memo[(m,f)] = 1
                return 1

            
            sum = 0
            if M-m >= 1:
                sum += recursion(m+1,f)
            if F-f >= 1:
                sum += recursion(m,f+1)
            memo[(m,f)] = sum
            return sum
        
        return recursion(0,0)
                            
if __name__ == '__main__':        
            
    sln    = Solution()    

    M      = 20
    F      = 10
    tStart = time.time()
    ans    = sln.noEqualPartition(M,F)
    tCost  = time.time() - tStart
    print('M,F={0},{1}, ans={2}, tCost={3:6.3f}(sec)'.format(M,F,ans,tCost))        
    