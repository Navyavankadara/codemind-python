n=input()
c=0
for i in n:
    if (i.isalpha()!=True and i.isdigit()!=True and i!=" "):
        c=c+1
print(c)