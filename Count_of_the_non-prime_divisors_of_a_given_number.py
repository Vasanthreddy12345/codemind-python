def p(n):
    f=0
    for i in range(2,n):
        if n%i==0:
            f+=1
    if  f==0:
        return False
    else:
        return True
m=int(input())
c=0
for j in range(1,m+1):
    if m%j==0 and p(j):
       c=c+1
print(c+1)