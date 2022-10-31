n=int(input())
m=int(input())
if n==1:
    n=2
for i in range(n,m+1):
    s=0
    for j in range(2,i):
        if i%j==0:
            s=1
    if s==0:
        print(i)