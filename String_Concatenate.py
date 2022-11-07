n=input()
m=input()
s=n+m
l=[]
for i in range(len(s)):
    l.append(s[i])
l.sort()
k=''
for i in l:
    k=k+i
print(k)