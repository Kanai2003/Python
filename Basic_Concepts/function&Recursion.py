#sum of two number usng functions
def sum(a, b):
    return a+b

print("Sum = ",sum(5,98))



#swap by function
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b

print("After swap : ",swap(5,10))



#fibonachi by function  
def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

print("Fibonachi number = ",fibo(5))   



#factorial by function
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

print("Factorial = ",factorial(5))



#Default parameter value // without passing any value to function
def greeting(name = "strangers"):
    return "Hello " + name

print(greeting())      # By default stranger will be value
print(greeting("Kanai"))