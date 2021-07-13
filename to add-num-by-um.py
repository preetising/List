list=[[20,12,50,45,90],
    [19,43,67,98,17],
]
i=0
sum=0
while i<len(list):
    j=0
    while j<len(list[i]):
        sum=list[0][j]+list[1][j]
        print(sum)
        j=j+1
    i=i+1