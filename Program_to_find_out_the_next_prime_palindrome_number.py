n=int(input())
n+=1
while True:
    s=str(n)
    if s==s[::-1]:
        is_prime=True
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                is_prime=False
                break
        if is_prime==True:
            print(n)
            break
    n+=1