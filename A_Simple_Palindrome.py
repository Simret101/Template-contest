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

def solve():
    n=hi()
    ans=['a','e','i','o','u']
    s=""
    full=n//5
    carry=n%5
    for i in range(5):
        s+=ans[i]*full
        if carry:
            s+=ans[i]
            carry-=1
    return s
for _ in range(hi()):
    print(solve())

