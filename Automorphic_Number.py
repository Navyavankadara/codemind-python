n=int(input())  
c=len(str(n))  
sq=n**2 
ld=sq%pow(10,c)
if ld==n:  
  print("Automorphic Number") 
else:  
  print("Not an Automorphic Number")  