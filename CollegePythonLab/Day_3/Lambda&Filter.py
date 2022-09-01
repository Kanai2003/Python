odd = lambda x : True if x%2 == 1 else False
x=[1,2,3,4,5,6,7,8,9]
z=filter(odd,x)
for i in z:
    print(i)