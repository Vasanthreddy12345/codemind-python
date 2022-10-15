n=int(input())
l=list(map(int,input().split()))
f=[]
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            f.append(j)
h=[]
for i in f:
    if f.count(i)==n:
        h.append(i)
print(max(h))