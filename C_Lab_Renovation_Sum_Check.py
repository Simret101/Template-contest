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
ans=[]
n=hi()
for _ in range(n):
    ans.append(hey())
for i in range(len(ans)):
    for  j in range(len(ans)):
        if ans[i][j]!=1:
            for k in range(len(ans)):
                if i!=k and ans[i][j]-ans[k][j] in ans[i]:
                    break

            else:
                print("No")
                exit(0)
print("Yes")

    