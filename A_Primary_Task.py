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
    n=hello()
    ans=n[2:]
    ans1=n[:2]
    if len(n)>=3 and int(ans)>=2 and int(ans1)==10 and int(n[2])!=0:
        res="YES"
    else:
        res="NO"
    return res
for _ in range(hi()):
    print(solve())



