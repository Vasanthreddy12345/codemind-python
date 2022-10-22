n=int(input())
c=0
b=[]
while(n>0):
    c+=1
    r=n%10
    n=n//10
    if r not in b:
        b.append(r)
x=len(b)
if(x==c):
    print("Unique Number")
else:
    print("Not Unique Number")