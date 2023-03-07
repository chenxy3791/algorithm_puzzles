# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:35:28 2021

@author: chenxy
"""

import sys
import time
from datetime import datetime
import math
# import random
from   typing import List
from   collections import deque
import itertools as it
import numpy as np
import calendar

#  Set SUNDAY to the first weekday
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2014,4)
print(np.array(calendar.monthcalendar(2014,4)))

def readfile(filename:str)->dict:
    '''
    Read holiday file and extra-workday file
    Parameters
    ----------
    filename : string        
    Returns
    -------
    A dictionary to store the data

    '''    
    print('Read {0} line by line, and store the holidays into a dictionary...'.format(filename))
    dat = dict()
    f=open(filename,'r')
    if f.mode == 'r':
        f_lines = f.readlines()
        for line in f_lines:
            # print(line,end='')
            date_object = datetime.strptime(line[:10], "%Y/%m/%d") # Strip the last '\n' in line
            # print("date_object ={}-{}-{}".format(date_object.year,date_object.month,date_object.day))        
            y,m,d = date_object.year,date_object.month,date_object.day
            if (y,m) not in dat:
                dat[(y,m)] = []
            dat[(y,m)].append(d)        
    f.close()
    return dat

# 1. Read the data file
h = readfile('q62-holiday.txt')
e = readfile('q62-extra-workday.txt')
    
# 2. Construct the dictionary for rectangulars area-shape pair
area_shape = dict()
for i in range(1,6):
    for j in range(1,8):
        if i*j not in area_shape:
            area_shape[i*j] = []
        area_shape[i*j].append((i,j))
        
# 3. loop over year/month to find the maximum rectangular of each month
max_area = dict()
for y in range(2014,2015):
    for m in range(4,7):
        # calendar.prmonth(y,m)
        c = np.array(calendar.monthcalendar(y,m))
        # Set the first and the last column to 0
        c[:,0] = 0
        c[:,6] = 0
        
        # print('The original month calendar:\n',c)
        # find the first weekday of the current month
        fst_wkday, num_days = calendar.monthrange(y, m)
        fst_wkday = (fst_wkday + 1)%7 # Because the SUNDAY is set to the first weekday
        
        # Set holidays to 0
        if (y,m) in h:
            holidays = h[(y,m)]
            for hday in holidays:
                # Find the position of the current holiday in month calendar matrix
                i = (hday + fst_wkday - 1)//7
                j = (hday + fst_wkday - 1)%7
                c[i,j] = 0

        # Set extra-workday to 100--any positive value is OK
        if (y,m) in e:
            extras = e[(y,m)]
            for eday in extras:
                # Find the position of the current extra workday in month calendar matrix
                i = (eday + fst_wkday - 1)//7
                j = (eday + fst_wkday - 1)%7
                c[i,j] = 100        
        # print('The month calendar after holidays and extra workdays setting:\n',c)
        # Search for the maximum rectangular only covering workday
        found = False
        for a in range(35,0,-1):
            # print(a)
            if a in area_shape:
                ij_list = area_shape[a]
                for (i,j) in ij_list:
                    for i0 in range(5-i+1):
                        for j0 in range(7-j+1):
                            rect = c[i0:i0+i,j0:j0+j]
                            # print(a,i,j,i0,j0, rect)
                            if np.all(rect):
                                max_area[(y,m)] = a
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break

print(max_area)
