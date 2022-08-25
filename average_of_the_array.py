n=int(input())
t=list(map(int,input().split()))
s=sum(t)
a=s/n
print("{:.2f}".format(a))