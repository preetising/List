list=["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
i=0
a=[]
b=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        b.append(list[i])
    i=i+1
print("new list=",b)