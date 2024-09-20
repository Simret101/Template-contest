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
c=str(int(n)+int(n1)).replace('0','')
ans=n.replace('0',"")

ans1=n1.replace('0',"")


if int(ans)+int(ans1)==int(c):
    print("YES")
else:
    print("NO")