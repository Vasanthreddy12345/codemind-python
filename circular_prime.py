def prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0:
            fc=fc+1
    if fc==2:
        return 1
    else:
        return 0
n=int(input())
m=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if prime(m)==1 and prime(rev)==1:
    print("circular prime")
elif prime(m)==1:
    print("prime but not a circular prime")
else:
    print("not prime")