import csv
a=open("desp.csv","r")
b = open("S.txt", "w")
c=a.readlines()
a=len(c)
for i in range(0,a):
    if i<5:
         g=b.write(c[i])
b.close()
b = open("S.txt", "r")
k=b.readlines()
print(k)