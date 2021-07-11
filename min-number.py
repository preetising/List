list=[10,100,80,28,18,26]
i=0
min=list[0]
while i<len(list):
	if list[i]<min:
		min=list[i]
	i=i+1
print("smallest number of list",min)