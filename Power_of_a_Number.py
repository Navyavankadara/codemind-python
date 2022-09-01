import math
x,y,m=map(int,input().split())
t=math.pow(x,y)
print(int(t%m))