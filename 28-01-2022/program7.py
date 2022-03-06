import csv
a=open("desp.csv","r")
b = open("m.txt", "w")
c = open("k.txt", "w")
e = a.readlines()
p=len(e)
for i in range(0,p):
    if(i%2!=0):
        b.write(e[i])
    else:
        c.write(e[i])
b.close()
b=open("m.txt","r")
l=b.readlines()
print("\n",l)
c.close()
c=open("k.txt","r")
h=c.readlines()
print("\n",h)