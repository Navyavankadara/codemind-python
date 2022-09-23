n=int(input())
m=list(map(int,input().split()))
s=0
p=0
l=len(m)
t=l//2
for i in m:
    if i<=t:
        s+=i
    elif i>t:
        p+=i
print(abs(s-p))
