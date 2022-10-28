a=int(input())
b=int(input())
for i in range(a,b+1):
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc+=1
    if fc==2:
        print(i)