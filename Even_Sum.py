n=int(input())
t=list(map(int,input().split()))
sum=0
for i in range(n):
    if t[i]%2==0:
        sum=sum+t[i]
print(sum)
        