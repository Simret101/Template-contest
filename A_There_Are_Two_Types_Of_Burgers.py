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
    a,b,c=hey()
    ans2=hey()
    res1=a-b-c
    if res1==0:
        res1=1
    res3=[res1,a,b,c]
    res3.sort()
    ans2.sort()
    ans=ans2[0]*res3[0]
    ans3=ans2[1]*res3[1]
    res4=ans+ans3
    if res4<0:
        return 0
    else:
        return res4
for _ in range(hi()):
    print(solve())


