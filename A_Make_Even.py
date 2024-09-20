import sys
import math, heapq, random
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd

INF=1e9
 
def hi():return int(sys.stdin.readline().strip())

def hey():return list(map(int, sys.stdin.readline().strip().split()))

def hello():return sys.stdin.readline().strip()
 
 
def howdy():return sys.stdin.readline().strip().split()
 
 
def hi_dig():return [int(i) for i in (list(sys.stdin.readline().strip()))]
 
 
def hel():return list(sys.stdin.readline().strip())


for _ in range(hi()):

    ans=list(map(int,hello()))
    res=-1
    if ans[-1]%2==0:
        
        res=0

      
    elif ans[0]%2==0:
    
        res=1

      
    elif ans[0]%2!=0 and ans[-1]%2!=0:
        count=0
        for i in range(0,len(ans)):
            if ans[i]%2==0:
                count+=1
        if count>0:
            res=2
    
    print(res)

    

