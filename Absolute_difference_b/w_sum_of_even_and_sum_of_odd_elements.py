n=int(input())
t=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(n):
    if t[i]%2==0:
        sum1=sum1+t[i]
    if t[i]%2!=0:
        sum2=sum2+t[i]
print(abs(sum1-sum2))