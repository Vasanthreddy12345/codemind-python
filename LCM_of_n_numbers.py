n=int(input())
l=list(map(int,input().split()))
f=[]
for i in l:
    for j in range(1,1000):
        f.append(j*i)
h=[]
for i in f :
    if f.count(i)==n:
        h.append(i)
print(min(h))