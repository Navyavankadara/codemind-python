n=int(input())
m=list(map(int,input().split()))
sum=0
for i in range(n):
    sum=sum+m[i]
print(sum)