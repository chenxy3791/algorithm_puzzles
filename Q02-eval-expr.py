# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 08:55:36 2021

@author: chenxy
"""
import time
import random
# from   queue import Queue
from   typing import List
from   collections import deque
    
class Solution:

    def exprEval(self, expr: str) -> int:
        """
        :expr:  A string representing a fundamental expression to be evaluated
        :    
        :ret:  return the evaluation result
        """ 
        q = deque()
        k = 0

        # Handling of multi-digit number
        prev_is_digit = False        
        while k < len(expr):
            a = expr[k]
            if a.isdigit():
                if prev_is_digit:                   
                    q.append(int(a) + 10*q.pop())
                else:
                    q.append(int(a))
                    prev_is_digit = True
            else: 
                prev_is_digit = False
                q.append(a)    
            k = k + 1        

        # Handling of '*' and '/'
        # print(q)
        q1 = deque()        
        while len(q) > 0:
            a = q.popleft()
            if a == '*':
                rslt = q1.pop() * q.popleft()
                q1.append(rslt)
            elif a == '/':
                d = q.popleft()
                if d != 0:
                    rslt = q1.pop() // d  # Currently, assuming only integer division here 
                else:
                    return float('inf')
                q1.append(rslt)
            else: #if isinstance(a,int) is True:
                q1.append(a)
            
        # Now, there should be only digits and '+', '-' left in the queue
        # print(q1)
        rslt = 0
        while len(q1) > 0:
            a = q1.popleft()
            if a == '+':
                rslt = rslt + int(q1.popleft())
            elif a == '-':
                rslt = rslt - int(q1.popleft())            
            else: #if isinstance(a,int):
                rslt = a

            # print(rslt)
        return rslt
                            
    
    def op_combination(self) -> List:    
        op  = ['+', '-', '*', '/','']
        ans = []
        
        for num in range(1000,10000):
            if (num % 10) == 0:
                continue
            
            numReverse = int(str(num)[::-1])
            # print('num = {0}, numReverse = {1}'.format(num,numReverse))
            for k1 in range(len(op)):
                for k2 in range(len(op)):
                    for k3 in range(len(op)):
                        if not(k1==4 and k2==4 and k3==4):
                            numStr = str(num)
                            expr   = numStr[0] + op[k1] + numStr[1] + op[k2] + numStr[2] + op[k3] + numStr[3]
                            rslt   = self.exprEval(expr)                            

                            if numReverse == rslt:
                                print('num={0}, numReverse={1}, expr={2}, rslt={3}'.format(num,numReverse,expr,rslt))
                                ans.append([num,op[k1],op[k2],op[k3]])
        return ans
                                
if __name__ == '__main__':        
    
    sln = Solution()

    # First, test exprEval()
    
    # expr = '1+2'
    # print(expr, ' = ', sln.exprEval(expr))

    # expr = '1+2-4*5'
    # print(expr, ' = ', sln.exprEval(expr))    

    # expr = '3*5+4-9'
    # print(expr, ' = ', sln.exprEval(expr))    

    # expr = '3*2+4/2'
    # print(expr, ' = ', sln.exprEval(expr))    

    # expr = '59*31'
    # print(expr, ' = ', sln.exprEval(expr))        
    
    # Sendondly, test op_combination()
    
    t1 = time.monotonic()
    ans = sln.op_combination()
    t2 = time.monotonic()    
    print('ans = {0}, tCost = {1}'.format(ans,(t2-t1)))
                                
                