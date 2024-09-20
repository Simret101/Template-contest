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
i=0
j=0
ans=[]
while i<len(n) and j<len(n1):
    if n[i]==n1[j] and n[i]=="1":
        ans.append("0")
    if n[i]==n1[j] and n[i]=="0":
        ans.append("0")
    if n[i]!=n1[j]:
        ans.append("1")
    i+=1
    j+=1
print("".join(ans))

