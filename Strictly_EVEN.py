n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(n):
    if m[i]%2==0 and i%2!=0:
        c+=1
if c==0:
    print("True")
else:
    print("False")
    
