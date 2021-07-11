user=int(input('enter a no'))
i=1
a=[]
while i <=(user):
	j=1
	b=[]
	a.append(i)
	while j<=10:
		d=j*i
		b.append(d)
		j+=1
	i+=1
	a.append(b)
print(a)