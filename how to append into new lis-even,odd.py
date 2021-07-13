a=int(input("enter value="))
i=0
c=[]

while i<(a):
    b=int(input("enter number="))
    c.append(b)
    i=i+1
print("orignal number list",c)
even=[]
odd=[]
j=0
while j<len(c):
    if c[j]%2==0:
        even.append(c[j])
    else:
        odd.append(c[j])
    j=j+1
print("even number list",even)
print("odd number list",odd)

 