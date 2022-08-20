n=int(input())
for i in range(n):
    p=list(map(int,input().split()))
    t=int(input())
    if t in p:
        print("True")
    else:
        print("False")