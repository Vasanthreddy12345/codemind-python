n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
      if j==i or j==n+1-i:
        print(n+1-i,"",end='')
      else:
          print(" ",end="")
    print()