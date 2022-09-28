p,r,t=map(int,input().split())
ci=p*(1+r*0.01)**t
print("{:.2f}".format(ci))