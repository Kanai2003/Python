def fib():
    f,s=0,1
    while True :
        yield f
        f,s=s,f+s

for x in fib():
    if x>50:
        break
    print(x,end=" ")