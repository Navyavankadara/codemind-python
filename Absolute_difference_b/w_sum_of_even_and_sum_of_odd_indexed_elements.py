n=int(input())
m=list(map(int,input().split()))
odd=0
even=0
for i in range(n):
    if i%2==0:
        even=even+m[i]
    else:
        odd=odd+m[i]
print(even-odd)