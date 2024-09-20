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
ans={1:["women","child"],2:"man",3:"rat",4:'captain'}
ans2=[]
for _ in range(hi()):

    key,val=howdy()
    ans2.append([key,val]) 

for i in range(len(ans2)):

    if ans2[i][1] in ans:
        ans2.append(ans["rat"])
    if "woman" in ans and "child" in ans:
        ans2.append(ans["woman"])
    if "child" in ans:
        ans2.append(ans["child"])
    if "man" in ans:
        ans2.append(ans["man"])
    if "captain" in ans:
        ans2.append(ans["captain"])
    for i in ans2:
        for j in i:
            print(j)

