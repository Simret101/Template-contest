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


ans=sorted(hey())
res=max(ans)
res2=Counter(ans)
if ans[0]+ans[1]>ans[2] or  ans[1]+ans[2]>ans[3]:
    print("TRIANGLE")
elif ans[0]+ans[1]==ans[2] or  ans[1]+ans[2]==ans[3]:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
