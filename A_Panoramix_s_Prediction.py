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
ans=[2,3,5,7]
for  i in  range(4,51):
    if i%2!=0 and i%5!=0 and i%3!=0 and i%7!=0:
        ans.append(i)
n,m=hey()
for i in range(1,len(ans)):
    if ans[i-1]==n and ans[i]==m:
        print("YES")
        break
else:
    print("NO")