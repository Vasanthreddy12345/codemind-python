n=int(input())
m=int(input())
for i in range(n,m+1):
    rev=0
    k=i
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if rev==k:
        print(k,end=" ")