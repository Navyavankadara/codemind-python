n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
c=0
for i in l:
    if i not in a:
        if k==l.count(i):
            c+=1
            a.append(i)
if c==0:
    print("-1")
else:
    for i in a:
        print(i,end=" ")