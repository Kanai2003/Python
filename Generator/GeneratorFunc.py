from re import I
from tkinter import N
from pkg_resources import yield_lines


def new (dict):
    for x,y in dict.items():
        yield x,y;

a = {1:"hi" , 2:"welcome" }
b=new(a)
print(b)
print(next(b))
print(next(b))



def myFunc(i) :
    while i<=3:
        yield i 
        i+=1

j=myFunc(2)
print(next(j))
print(next(j))




def ex():
    n=3
    yield n
    n=n*n
    yield n

v=ex()
print(next(v))
print(next(v))




def sum():
    n=1
    yield n
    n = n+1
    yield n

r=sum()
for i in r:
    print(i)




f=range(10)
print("List comp",end=":")
q=[x+2 for x in f]
print(q)
print("gen comp",end=":")
r=(x+2 for x in f)
print(r)
for x in r:
    print(x)
