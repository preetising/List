list=[1,2,4,8,16,32,64,128]
i=0
multi=1
c=[]
while i<len(list):
	multi=list[i]*multi
	c.append(list[i])
	i=i+1
print(c)