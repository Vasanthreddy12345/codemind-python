n=int(input())
for _ in range(n):
    m=int(input())
    np=m
    while True:
        is_prime=True
        for i in range(2,int(np**0.5)+1):
            if np%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        np+=1 
    pp=m
    while True:
        is_prime=True
        for i in range(2,int(np**0.5)+1):
            if pp%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        pp-=1 
    if m-pp<=np-m: 
        print(pp)
    else:
        print(np)
    
    