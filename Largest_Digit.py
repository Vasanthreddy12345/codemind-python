n=int(input())
ld=0
while n>0:
    r=n%10
    if r>ld:
        ld=r
    n=n//10
print(ld)