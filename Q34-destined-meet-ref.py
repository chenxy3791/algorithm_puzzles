# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 09:20:45 2021

@author: chenxy
"""

import time
n=6
cnt=0
t1=time.perf_counter()

def search(manX,manY,wX,wY,meetTimes):
    global cnt
    #print(manX,manY,wX,wY,meetTimes)
    if manX>n or manY>n or  wX<0 or wY<0:
        return
    if manX==n and manY==n and wX==0 and wY==0 and meetTimes>=2:
        cnt+=1
        return
    if manX==wX:
        meetTimes+=1
    if manY==wY:
        meetTimes+=1
    search(manX+1,manY,wX-1,wY,meetTimes)
    search(manX+1,manY,wX,wY-1,meetTimes)
    search(manX,manY+1,wX-1,wY,meetTimes)
    search(manX,manY+1,wX,wY-1,meetTimes)
    
def search1(manX,manY,wX,wY,meetTimes):
    global cnt
    if manX==n and manY==n and wX==0 and wY==0 and meetTimes>=2:
        cnt+=1
        return
    if manX<=n and manY<=n and  wX>=0 and wY>=0:
        if manX==wX:
            meetTimes+=1
        if manY==wY:
            meetTimes+=1
        search(manX+1,manY,wX-1,wY,meetTimes)
        search(manX+1,manY,wX,wY-1,meetTimes)
        search(manX,manY+1,wX-1,wY,meetTimes)
        search(manX,manY+1,wX,wY-1,meetTimes)
    
search(0,0,n,n,0)
print(cnt)                  #527552
print(time.perf_counter()-t1)  