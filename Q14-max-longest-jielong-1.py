# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 08:17:34 2021

@author: chenxy
"""

import sys
import time
import datetime
import math
# import random
from   typing import List
# from   queue import Queue
# from   collections import deque
# import itertools as it

country_list = ["Brazil", "Croatia", "Mexico",
                "Cameroon", "Spain", "Netherlands",
                "Chile", "Australia", "Colombia",
                "Greece", "Cote d'Ivoire", "Japan",
                "Uruguay", "Costa Rica", "England",
                "Italy", "Switzerland", "Ecuador",
                "France", "Honduras", "Argentina",
                "Bosnia and Herzegovina", "Iran", "Nigeria",
                "Germany", "Portugal", "Ghana",
                "USA", "Belgium", "Algeria",
                "Russia", "Korea Republic" ]
 
longest_jielong = []
 
def jielong_explore(visited, unvisited):
    """
    Parameters
    ----------
    visited   : list of conuntry names already visited
    unvisited : list of conuntry names not yet visited        
    Returns   : None
    """
    
    isNxtFound = False
    if len(unvisited) != 0: # There are countries not yet visited, continue the exploration.
        for index, c in enumerate(unvisited):
            if c[0] == visited[-1][-1]:
                jielong_explore(visited + [c], unvisited[:index] + unvisited[index + 1:])
                # jielong_explore(visited.append(c), unvisited[:index] + unvisited[index + 1:])
                isNxtFound = True
                
    # If there is no next country found, then the current jielong path is finished,
    # Compare the length of the current jielong with the recorded longgest jielong and update accordingly.
    if not isNxtFound or len(unvisited) == 0:
        global longest_jielong
        if len(longest_jielong) < len(visited):
            longest_jielong = visited
    
# Convert all country names to upper case for the convenience of processing.
for k in range(len(country_list)):
    country_list[k] = country_list[k].upper()

# Start from each country for a new jielong game
tStart = time.time()
for i, country in enumerate(country_list):
    jielong_explore([country], country_list[:i]+country_list[i+1:])
tCost  = time.time() - tStart

print("The max length of JieLong = {0}\n{1}\ntCost={2:6.3f}(sec)".format(len(longest_jielong), longest_jielong,tCost))
