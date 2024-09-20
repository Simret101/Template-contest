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


for _ in range(hi()):
    n=hi()
    ans=hey()
    stack=[ans[0]]
    stack2=[]
    for i in range(1,len(ans)):
        
      
        ans3=stack[-1]
        res=ans[i]-ans3
        stack2.append(res)

        stack.pop()
        stack.append(res)
    print(stack2)
    if stack2[0]==1:
        res4=sum(stack2)
        print(res4-1)
    else:       
        print(sum(stack2))
    