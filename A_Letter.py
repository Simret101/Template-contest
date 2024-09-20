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

a,b=hey()
ans=[hello() for _ in range(a)]
top, bottom, left, right= a,0,b,0
for i in range(a):
    for j in range(b):
        if ans[i][j] =="*":
            top,bottom,left,right=min(top,i),max(bottom,i),min(left,j),max(right,j)
for i in range(top,bottom+1):
    print(ans[i][left:right+1])


        