import sys
import math, heapq, random
import re
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



n=hello().lower()
n1=hello().lower()

count=0
count1=0
i,j=0,0
while i<len(n) and j<len(n1):
    if ord(n[i])>ord(n1[i]):
        print(1)
        break
    elif ord(n[i])<ord(n1[i]):
        print(-1)
        break
    i+=1
    j+=1
else:
    print(0)


