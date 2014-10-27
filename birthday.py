def f(n,a=1):
    for i in range(0,n):
        a=a*(((365-n)/365))
        return(1-a)