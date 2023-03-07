# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:55:14 2021

@author: chenxy
"""

class Solution:
    def climbingStairs(self, N: int) -> int:
        """
        :N:    The total number of stairs between the two ends
        :    
        :ret:  return the number of combinations
        """        
        
        # Initialization
        f    = N * [0]
        f[0] = 1
        f[1] = 0

        memo = dict()
        memo[0] = 1
        memo[1] = 0
        
        def recursive(K):
            if K in memo:
                return memo[K]

            rslt = 0                                    
            for Ak in range(1,min(4,K-1)+1): # range doesn't include the upper bound, hence '+1' is needed here.
                for Bk in range(1,min(4,K-1)+1):
                    sub = K-(Ak+Bk)
                    if sub >= 0:
                        sub_rslt = recursive(sub)    
                        rslt += sub_rslt
                        
            memo[K] = rslt
            return rslt                        

        return recursive(N)                
                    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()

    N    = 10
    t1 = time.monotonic()
    rslt = sln.climbingStairs(N)
    t2 = time.monotonic()    
    print('N = {0}, rslt = {1}, tCost = {2}'.format(N,rslt,(t2-t1)))

    N    = 100
    t1 = time.monotonic()
    rslt = sln.climbingStairs(N)
    t2 = time.monotonic()    
    print('N = {0}, rslt = {1}, tCost = {2}'.format(N,rslt,(t2-t1)))    