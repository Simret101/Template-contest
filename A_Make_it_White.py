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
    ans=deque(hello())
    while len(ans)>0 and ans[0]=="W":
        ans.popleft()
    while len(ans)>0 and ans[-1]=="W":
        ans.pop()
    return len(ans)


    
    
for _ in range(hi()):
    print(solve())
                  
