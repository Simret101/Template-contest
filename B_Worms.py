import sys
import math, heapq, random
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd 
 


 
def hi():
    return int(sys.stdin.readline().strip())
 
 
def hey():
    return list(map(int, sys.stdin.readline().strip().split()))
 
 
def hello():
    return sys.stdin.readline().strip()
 
 
def howdy():
    return sys.stdin.readline().strip().split()
 
 
def hi_dig():
    return [int(i) for i in (list(sys.stdin.readline().strip()))]

def hel():
    return list(sys.stdin.readline().strip())

n=hi()
ans=hey()
m=hi()
ans1=hey()
prefix_=0
res=[]
for i in range(n):
    prefix_+=ans[i]
    res.append(prefix_)
for j in ans1:
    last_ans=bisect_left(res,j)
    print(last_ans+1)