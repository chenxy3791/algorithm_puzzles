# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 10:13:26 2021

@author: chenxy
"""

import sys
import time
import random
# from   typing import List

class Solution:
    def xor_yanghui1(self, N:int)->int:
        """
        :N:    Specify the serial-number of the zero to be searched
        :    
        :ret:  return the layer count
        """
        
        zeroCnt   = 0
        layerCnt  = 1
        prevLayer = [1]
        cmpFlg   = 0
        
        while(1):
            layerCnt += 1
            curLayer  = []  # Initialize the current layer to one empty list
            for k in range(len(prevLayer)-1):
                newData = (prevLayer[k]+prevLayer[k+1])%2
                curLayer.append(newData)
                if newData==0:
                    zeroCnt += 1
                    if zeroCnt == N:
                        # Because there are two layer of loop, we need an extra flag to indicate to
                        # exit from the outer layer of loop too.
                        cmpFlg = 1 
                        break
                
            if cmpFlg == 1:
                break
            else:
                # Update prevLayer for the computation of the next layer, by appending the two '1's 
                # in the head and tail.
                prevLayer = [1] + curLayer + [1]
        
        return layerCnt
    

    def xor_yanghui2(self, N:int)->int:
        """
        :N:    Specify the serial-number of zero to be searched
        :    
        :ret:  return the layer count
        """

        zeroCnt   = 0
        layerCnt  = 1
        prevLayer = 1
        
        while(1):
            layerCnt += 1
            curLayer = (prevLayer << 1) ^ prevLayer
            # Count the zero inside curLayer
            tmp = curLayer
            for k in range(layerCnt):                                
                zeroCnt += 1 - (tmp & 1) # Check whether the LSB is 0
                # print('layerCnt={0}, curLayer={1}, k={2}, tmp={3}, zeroCnt={4}'.format(layerCnt,curLayer,k,tmp,zeroCnt))
                tmp = tmp >> 1
            if zeroCnt >= N:
                break
            else:
                prevLayer = curLayer
        return layerCnt

    
if __name__ == '__main__':        
    
    sln = Solution()    
    
    N = 2014000
    t1 = time.monotonic()
    print('N = {0}, ans = {1}'.format(N, sln.xor_yanghui1(N)))
    t2 = time.monotonic()    
    print('N = {0}, ans = {1}'.format(N, sln.xor_yanghui2(N)))
    t3 = time.monotonic()    
    print('tCost1 = {0} sec, tCost2 = {1} sec'.format(t2-t1,t3-t2))