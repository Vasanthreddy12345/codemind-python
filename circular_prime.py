n=int(input())
m=n
rev=0
while m>0:
    r=m%10
    rev=rev*10+r
    m=m//10
is_prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
        break
is_prime1=True
for j in range(2,int(rev**0.5)+1):
    if rev%j==0:
        is_prime1=False
        break
if is_prime and is_prime1:
    print('circular prime')
elif is_prime:
    print('prime but not a circular prime')
else:
    print('not prime')