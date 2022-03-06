a=open("a.txt","r")
b=open("b.txt","w")
c=a.readlines()
print(c)
d=len(c)
for i in range(0,len(c)):
    if(i%2==0):
        b.write(c[i])
    else:
         pass
b.close()
b=open("b.txt","r")
e=b.read()
print(e)
a.close()
b.close()