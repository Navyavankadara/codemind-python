n=int(input())
m=list(map(int,input().split()))
k=int(input())
s=0
for i in m:
    if i==k:
        s+=i
        break
    else:
        s+=i
print(s)
        