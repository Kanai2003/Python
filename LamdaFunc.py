x = lambda a: a*a
print(x(5))

# lambda within user defined function---------------------
def A(x):
    return(lambda y:x+y)

t = A(5)         # here passing the value of 'x'
print(t(2))      # here passing the value of 'y' by 't'
print(t(3))

u = A(10)
print(u(9))



# using lambda function within filter()--------------------------
# syntex: filter(function,iterable)
'''
    here filter function will check with help of lambda function that is 
    there any element present in "myList" which if we divide it by 3 will be 2, if true 
    then store it's value in "newList"
'''
myList = [1,2,3,4,5,6,7,8,9]

newList1 = list(filter(lambda a: (a/3 ==2),myList))
newList2 = list(filter(lambda a: (a%2 != 0),myList))
print(newList1)
print(newList2)


# lambda function within map()---------------------------------
# map(): Applies a given function to all the iterable and returnsa new list as true/false

newList3 = list(map(lambda a :(a/2 != 3) , myList))
newList4 = list(map(lambda a : (a%2 ==0), myList))
print(newList3)
print(newList4)


# lambda function within reduce()------------------------------
# syntex: reduce(function,sequence)
from functools import reduce
res = reduce(lambda a,b :a+b , [23,45,25,67,97])
print(res)      #here lambda function will do :((((23+45)+25)+67)+97) and return the total value
newList5 = reduce(lambda a,b:a*b , myList)   #similerly , multiplies all elements of "myList" and return total value
print(newList5)



# lambda for algebra--------------------------------------
# linear equation
le1 = lambda a :a*a
print(le1(9))
le2 = lambda a,b : 3*a +4*b
print(le2(4,5))

# quadratic equation
qe1 = lambda a,b :(a+b)**2    #(a+b)^2
print(qe1(3,4))


