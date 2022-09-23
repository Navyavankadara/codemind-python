n=int(input())
m=list(map(int,input().split()))
s=0
for i in m:
    if i%2!=0:
        break
    else:
        s+=i
print(s)
    