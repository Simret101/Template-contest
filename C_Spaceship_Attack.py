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

n,m=hey()
ans=hey()
ans2=[]
for _ in range(m):
    k,m=hey()
    ans2.append([k,m])
ans2.sort( )
ans3=[0]
for i in range(len(ans2)):
    
    ans3.append(ans3[-1]+ans2[i][1])
print(ans3)
#ans4=[ans3[i][0] for i in range(len(ans3))]

for j in ans:
    print(bisect_right(ans3,j),end=" ")   

