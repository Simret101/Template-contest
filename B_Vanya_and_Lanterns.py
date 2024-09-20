
n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
maxi=float(a[0])
for i in range(1,n):
    m=(a[i]-a[i-1])/2
    maxi=max(maxi,m)
   
m=l-a[-1]
if maxi<m:
    maxi=m
print(maxi) 