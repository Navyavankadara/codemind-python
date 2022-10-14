n=int(input())
a=n
b=n
while True:
    is_prime=True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            is_prime=False
            break
    if is_prime==True:
        break
    else:
        a-=1
while True:
    is_prime=True
    for i in range(2,int(b**0.5)+1):
        if b%i==0:
            is_prime=False
            break
    if is_prime==True:
        break
    else:
        b+=1
c1=abs(n-a)
c2=abs(b-n)
print(min(c1,c2))

    