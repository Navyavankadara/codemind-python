n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in l:
    if i not in a:
        if i==l.count(i):
            c+=1
            a.append(i)
if c==0:
    print("0")
else:
    print(c)