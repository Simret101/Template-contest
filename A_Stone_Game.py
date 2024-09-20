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
    ans=hey()
    maxi=max(ans)
    mini=min(ans)
    res1=ans.index(mini)
    res2=ans.index(maxi)
    x=len(ans)-1
    print(res1,res2)
    ans1=min(res1-0,n-res1)
    ans2=min(res2-0,n-res2)
    return ans1+ans2

for _ in range(hi()):
    print(solve())