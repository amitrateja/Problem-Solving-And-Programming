f=open("python.txt","r")
r=f.read()
print(r)
print("\n")

print("number of characters are",len(r))
print("\n")

c=0
for i in r:
    if i=="\n":
        c=c+1
print("number of lines are",c+1)
print("\n")

k=r.split()

print("number of words are",len(k))
print("\n")


from collections import Counter


y=dict(Counter(k))



print("repeated words are : number of times repeated")
for i in y:
    if y[i]!=1:
        print({i:y[i]})
        


