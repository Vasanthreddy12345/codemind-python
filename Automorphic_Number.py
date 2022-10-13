n=int(input())
s=n*n
t=n
dc=0
while n>0:
    n=n//10
    dc+=1
x=s%10**dc
if x==t:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
