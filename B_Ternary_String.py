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
    ans=list(hello())
    mini=INF
    store={'1':0,'2':0,'3':0}
    j=0
    for i in range(len(ans)):
        store[ans[i]]+=1
        while store[ans[j]]>1:
            store[ans[j]]-=1
            j+=1
        if store['1']>0 and store['2']>0  and store['3']>0:
            mini=min(mini,i-j+1)
    if mini==INF:
        mini=0


    return mini
for _ in range(hi()):
    print(solve())
