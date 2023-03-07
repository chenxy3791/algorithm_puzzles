# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:35:55 2021

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
    def dateConversion(self, startDate: str, endDate: str) -> List:
        """
        :startDate: The state date in string format   
        :endtDate:  The end date in string format        
        :ret:       The list of dates in string format satisfying condition
        """                

        ans = []
                                                    
        # Iteration up to endDate, by increment 1 per iteration
        date = startDate
        while 1:
            # print(date)
            # Date --> string format
            dateStr  = str(date)
            # Remove '-' in the string format, for example, '1966-07-23'-->'19660723'
            dateStr1 = dateStr.replace('-','',-1)
            # Conver to integer and then to bin            
            dateBin = bin(int(dateStr1))[2:]
            if dateBin == dateBin[::-1]:
                ans.append((date))
            
            if date == endDate:
                break
            
            date += datetime.timedelta(days=1)        
        return ans
                
if __name__ == '__main__':        
            
    sln    = Solution()    

    tStart = time.time()
    start  = datetime.date(1964,10,10)
    end    = datetime.date(2020,7,24)
    ans    = sln.dateConversion(start,end)
    tCost  = time.time() - tStart
    print('start={0}, end={1}, tCost = {2}(sec)'.format(start,end,tCost))        
    for k in range(len(ans)):
        print('date = {0}: {1}'.format(k,ans[k]))