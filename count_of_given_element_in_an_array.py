n=int(input())
m=list(map(int,input().split()))
z=int(input())
if z in m:
    print(m.count(z))
 
else:
    print("0")