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

for _ in range(hi()):
    n=hi()
    res=n%10
    res2=10*(res-1)
    digit_len=len(str(n))
    for i in range(1,digit_len+1):
        res2+=i
    print(res2)


 