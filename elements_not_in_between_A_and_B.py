n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in range(n):
    if m[i]<a or m[i]>b:
        print(m[i],end=" ")
        c+=1
if c==0:
    print("-1")