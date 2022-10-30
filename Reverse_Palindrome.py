def rp(n):
    k=n
    rev=0
    while n>0:
         r=n%10
         rev=rev*10+r
         n=n//10
    if rev==k:
        return rev
    else:
        return rp(rev+k)
m=int(input())
p=m
d=0
while p:
    h=p%10
    d=d*10+h
    p=p//10
print(rp(d+m))
