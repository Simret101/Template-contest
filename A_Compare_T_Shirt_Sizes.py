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

for _ in  range(hi()):
    ans1,ans2=howdy()
    
    if ord(ans1[-1])==ord(ans2[-1]) and ans1[-1]=="S":
        res=len(ans1)-1
        res2=len(ans2)-1
        if res2<res:
            print("<")
        elif res2>res:
            print(">")
        else:
            print("=")
    elif ord(ans1[-1])==ord(ans2[-1]) and ans1[-1]=="L":
        res=len(ans1)-1
        res2=len(ans2)-1
        if res2>res:
            print("<")
        elif res2<res:
            print(">")
        else:
            print("=")
    elif ord(ans1[-1])>ord(ans2[-1]):
        print("<")
    elif ord(ans1[-1])<ord(ans2[-1]):
        print(">")
