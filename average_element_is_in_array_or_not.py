n=int(input())
t=list(map(int,input().split()))
s=sum(t)
a=s//n
if a in t:
    print("True")
else:
    print("False")