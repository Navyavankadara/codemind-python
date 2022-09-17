n=int(input())
m=list(map(int,input().split()))
c=0
l=[]
for n in m:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            c+=1
            l.append(n)
            t=sum(l)/c
print("{:.2f}".format(t))
