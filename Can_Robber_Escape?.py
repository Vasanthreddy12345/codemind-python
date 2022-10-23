n=int(input())
a=list(map(int,input().split()))
f=0
for i in a:
    if i<n:
        f=1
    else:
        f=0
        break
if f==1:
    print("YES")
else:
    print("NO")