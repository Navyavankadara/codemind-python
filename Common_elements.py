n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
l=[]
for i in a1:
    if i in a2:
        if i not in l:
            l.append(i)
for i in l:
    print(i,end=" ")