n=int(input())
edc=odc=0
while n>0:
    r=n%10
    if r%2==0:
        edc +=1
    else:
        odc+=1
    n=n//10
if edc ==0:
    print("Odd")
elif odc ==0:
    print("Even")
else:
    print("Mixed")