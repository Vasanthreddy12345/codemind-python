n=int(input())
s=n*n
if n==s%10 or n==s%100 or n==s%1000:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')