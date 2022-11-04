n=int(input())
c=1
a=0
b=1
k=0
for i in range(0,n):
    print(a,end=' ')
    c=a+b
    a=b
    b=c