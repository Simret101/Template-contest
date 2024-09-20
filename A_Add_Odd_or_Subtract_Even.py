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
    a,b=hey()
    if a==b:
        return 0
    
    if a>b:
        x=a-b
        if x%2==0:
            return 1
        else:
            return 2

    else:
        x=b+a
        if x%2==1:
            return 1
        else:
            return 2
for _ in range(hi()):
    print(solve())