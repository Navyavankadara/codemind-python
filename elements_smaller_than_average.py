n=int(input())
m=list(map(int,input().split()))
c=0
t=sum(m)//n
for i in range(n):
    if m[i]<=t:
        c+=1
print(c)
    