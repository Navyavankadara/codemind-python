n=int(input())
m=list(map(int,input().split()))
k=int(input())
c=0
for n in m:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            if n<=k:
                c+=1
print(c)