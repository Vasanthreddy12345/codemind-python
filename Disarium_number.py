n=int(input())
k=n
s=0
i=1
rev=0
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
while rev:
    r1=rev%10
    s+=r1**i
    rev=rev//10
    i+=1
if s==k:
    print('True')
else:
    print('False')