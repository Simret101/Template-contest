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
    n2=hi()
    n=str(n2)
    if n2<9:
        print(n2-1)
    else:
        res=int(n[0])-1
        
        ans=str(res)+n[1:]
        ans2=int(ans)
      
        print(ans2)
    