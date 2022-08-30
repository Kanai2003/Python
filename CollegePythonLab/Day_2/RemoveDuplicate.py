def remDup(*n):
    x=[]
    for i in n :
        if i not in x :
            x.append(i)
    return x

print(remDup(4,3,1,2,3,1,4,5))
print(remDup(3,2,1,2,3))