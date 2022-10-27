n,m=map(int,input().split())
while n!=0 and m!=0:
    if n>m:
        n%=m
    else:
        m%=n
if n==0:
    print(m)
else:
    print(n)