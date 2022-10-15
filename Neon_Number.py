n=int(input())
t=n*n
s=0
while t>0:
    r=t%10
    s+=r
    t=t//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")
