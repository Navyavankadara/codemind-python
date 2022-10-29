n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if(i==l.count(i)):
        a.append(i)
a.sort()
if(a==[]):
    print(-1)
else:
    print(a[0],end=" ")
    print(a[-1])