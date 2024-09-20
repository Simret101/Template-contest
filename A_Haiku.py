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

n=hello()
n1=hello()
n2=hello()
ans=[n,n1,n2]
ans2="YES"
for i in range(len(ans)):
    res=0
    for j in ans[i]:
       
        if j in "aeiou":
            res+=1
    if i==0 and res!=5:
        ans2="NO"
    if i==1 and res!=7:
        ans2="NO"
    if i==2 and res!=5:
        ans2="NO"
print(ans2)
