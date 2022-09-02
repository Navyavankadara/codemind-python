n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(n):
    if m[i]<a or m[i]>b:
        s+=m[i]
print(s)