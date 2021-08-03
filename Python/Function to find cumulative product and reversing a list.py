#function to find cumulative_product to compute cumulative product of a list of numbers

l=[]
n=int(input("Enter length of list:"))
for i in range(0,n):
    b=int(input("Enter element:"))
    l.append(b)
print("Entered list is:",l)
print("\n")
def cumulative_product(l):
    p=1
    for  i in l:
        p=p*i

    print("Product of all the values of list is ",p)
    print("\n")

cumulative_product(l)

#function to reverse a list

def rev_list(l):
    revl=[]

    for i in range(-1,-len(l)-1,-1):
        revl.append(l[i])

    print("List after reversing :",revl)

rev_list(l)




    
