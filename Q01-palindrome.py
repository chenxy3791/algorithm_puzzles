# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:55:36 2021

@author: chenxy
"""
import time
import random
    
class Solution:
    def palindrome(self, N: int) -> int:
        """
        :N:    The number of the smallest palindrome to be searched for
        :    
        :ret:  return the palindrome list
        """ 
        
        count = 0
        rslt  = []
        k = 11
        while (1):            
            if not (k%8==0 or k%10==0):
                if k%1001 == 0: # cannot use 'k%1000' as print condition!
                    print('k = {0}'.format(k))
                k_decstr = str(k)
                if k_decstr == k_decstr[::-1]: # aStr[::-1] return the reverse of the original one
                    k_binstr = bin(k)[2:]  # bin(k) will return '0bxxxx'
                    if k_binstr == k_binstr[::-1]:
                        k_octstr = oct(k)[2:]  # oct(k) will return '0oxxxx'
                        if k_octstr == k_octstr[::-1]:
                            rslt.append(k)
                            count += 1
                            print('Found: k = {0}, count = {1}'.format(k, count))
                            if count == N:
                                break
            k += 2 # Skip the even number
        
        return rslt

if __name__ == '__main__':        
    
    sln = Solution()

    N    = 2
    t1 = time.monotonic()
    rslt = sln.palindrome(N)
    t2 = time.monotonic()    
    print('N = {0}, rslt = {1}, tCost = {2}'.format(N,rslt,(t2-t1)))    
                            
                