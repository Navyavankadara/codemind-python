n=int(input())
m=list(map(int,input().split()))
t=set(m)
c=0
for i in t:
    if i%2!=0:
        c+=1
print(c)