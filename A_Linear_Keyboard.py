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

def solve():
    ans=hello()
    ans2=hello()
    res=0
    for i in range(1,len(ans2)):
        res+=abs((ans.index(ans2[i])+1)-(ans.index(ans2[i-1])+1))
    return res
for _ in range(hi()):
    print(solve())
