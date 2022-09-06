n,m=map(int,input().split())
if n>m:
    smaller=m
else:
    smaller=n
for i in range(1,smaller+1):
    if (n%i==0) and (m%i==0):
        t=i
print(t)