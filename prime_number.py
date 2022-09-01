n=int(input())
cnt=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            cnt+=1
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")
            