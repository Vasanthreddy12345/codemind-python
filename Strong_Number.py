n=int(input())
m=n
s=0
while n>0:
    r=n%10
    n=n//10
    fc=1
    for i in range(r,0,-1):
        fc=fc*i
    s=s+fc
if s==m:
    print('The number {} is a strong number'.format(m))
else:
    print('The number {} is not a strong number'.format(m))