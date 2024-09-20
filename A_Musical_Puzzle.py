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
    n=hi()
    ans=hello()
    res=set()
    for i in range(len(ans)-2):
        res2=ans[i:i+2]
        res.add(res2)
    res.add(ans[len(ans)-2:])
    return len(res)
for _ in range(hi()):
    print(solve())

