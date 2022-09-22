n=int(input())
m=list(map(int,input().split()))
t=set(m)
s=0
for i in t:
    if i%2==0:
        s+=1
print(s)
       