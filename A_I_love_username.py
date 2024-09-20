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


n=hi()
ans=hey()
mini=ans[0]
maxi=ans[0]
count2=0
count1=0
for i in range(n):
    if mini>ans[i]:
        count1+=1
        mini=ans[i]
    elif maxi<ans[i]:
        count2+=1
        maxi=ans[i]
print(count1+count2)
