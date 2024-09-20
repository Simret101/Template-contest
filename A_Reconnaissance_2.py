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

n=hi()
ans=hey()
res=[n,1]
mini_v=abs(ans[0]-ans[n-1])
for i in range(1,n):
    mini=abs(ans[i]-ans[i-1])
    if mini<mini_v:
        res=[i,i+1]
        mini_v=mini


print(*res)



