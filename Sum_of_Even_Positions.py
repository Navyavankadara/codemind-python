n=int(input())
m=list(map(int,input().split()))
even=0
for i in range(n):
    if i%2==0:
        even=even+m[i]
print(even)