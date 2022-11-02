a=int(input())
b=int(input())
sum=a+b
temp=sum
for j in range(2,int(sum**0.5)+1):  
    if sum%j==0:
        break
else:
    sum=sum+1

for n in range  (sum,1,-1):
    for i in range(2,int(sum**0.5)+1):
        if sum%i==0:
            break
    else:
        x=sum-temp
        print(x)
        break
    sum+=1