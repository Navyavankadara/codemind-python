n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
s1=set(a1)
s2=set(a2)
c=0
for i in s1:
    if i in s2:
        c+=1
print(c)