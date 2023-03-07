# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:21:23 2021

@author: chenxy
"""

import time

class Solution:

    def patchPanelConnect(self, num):

        memo = dict()

        def recur(num): # Recursive core
            if num == 0:
                print('patchPanelConnectFast(): invalid input parameter')
            if num == 1:
                #print('patchPanelConnect({0}) = {1}'.format(num,1))
                return 1

            if num in memo:
                return memo[num]
                        
            # using two-port patch panel as the first stage
            sum2 = 0
            for n1 in range(1, num//2+1): 
                for n2 in range(n1, num-n1+1): 
                    if n2 == (num - n1):
                        if n2 == n1:                        
                            sum2 = sum2 + recur(n1) * (recur(n1)+1)/2
                        else:
                            sum2 = sum2 + recur(n1) * recur(n2)
                            
            
            # using three-port patch panel as the first stage
            sum3 = 0
            for n1 in range(1, (num//3+1)): # 
                for n2 in range(n1,(num-n1)//2+1): # 
                    for n3 in range(n2,(num-n1-n2+1)):# n3 = n2,n2+1,...num-n1-n2
                        if n3 == (num - (n1 + n2)):
                            if n1 == n2 and n2 == n3:                            
                                sum3 = sum3 + recur(n1) * (recur(n1)+1) * (recur(n1)+2)/6
                            elif n1 == n2:
                                sum3 = sum3 + recur(n1) * (recur(n1)+1) * recur(n3)/2
                            elif n1 == n3:
                                sum3 = sum3 + recur(n1) * recur(n2) * (recur(n1)+1)/2
                            elif n2 == n3:    
                                sum3 = sum3 + recur(n1) * recur(n2) * (recur(n2)+1)/2                                
                            else:
                                sum3 = sum3 + recur(n1) * recur(n2) * recur(n3)
    
            #print('patchPanelConnect({0}) = {1}'.format(num,(sum2+sum3)))
            memo[num] = (sum2 + sum3)
            return (sum2 + sum3)

        return recur(num)

if __name__ == '__main__':

    sln   = Solution()

    # print('num = 7, ans = ', sln.patchPanelConnect(7))    
    # print('num = 10, ans = ', sln.patchPanelConnect(10))
    
    # Testcase1    
    for num in range(4,21,4):
        tStart = time.time()    
        numOfConnect = sln.patchPanelConnect(num)
        tElapsed = time.time() - tStart        
        print('num = {0:2.0f}, connect methods = {1:8.0f}, tCost = {2:6.3f}(sec)'.format(num, numOfConnect,tElapsed))

    # # Testcase2
    # print('Testcase2...')
    # for num in range(100,101):
    #     tStart = time.time()    
    #     memo = {}
    #     numOfConnect,memo  = sln.patchPanelConnectFast(num, memo)
    #     tElapsed = time.time() - tStart        
    #     print('num = {0}: {1} connect methods, time cost = {2}(sec)'.format(num, numOfConnect,tElapsed))
