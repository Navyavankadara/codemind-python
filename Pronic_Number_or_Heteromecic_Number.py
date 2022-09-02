import math
def pronic(num):
    i=0
    while i<=(int)(math.sqrt(n)):
        if n==i*i+1:
            return True
        i+=1
    return False
n=int(input())
if pronic(n):
    print("NO")
else:
    print("YES")