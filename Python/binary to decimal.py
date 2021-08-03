a=input("enter a binary number")
d=0
for i in range(0,len(a)):
    d=d+(int(a[i]))*(2**((len(a))-(i+1)))
print(d)

c=0
for i in range(1,d):
    if d%i==0:
        c=c+i
if c==d:
    print("perfect number")
else:
    print("not perfect number")
