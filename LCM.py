a,b=map(int,input().split())
if a>b:
    mx=a
else:
    mx=b
i=mx
while i>0:
    if i%a==0 and i%b==0:
        print(i)
        break
    i+=mx
    