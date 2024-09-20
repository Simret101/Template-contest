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

def  solve():
    n, k = hey()
    a = hey()
    res = 0
    for i in range(30, -1, -1):
        count = 0
        for num in a:
            if num & (1<<i):
                count+=1
        if n - count <= k:
            k -= (n - count)
            res += (1<<i)
    return res
for _ in range(hi()):
    print(solve())