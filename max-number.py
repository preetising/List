list=[10,20,30]
i=0
max=list[0]
while i<len(list):
	if list[i]>max:
		max=list[i]
	i=i+1
print("largest number",max)