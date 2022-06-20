'''
5 types of dataTypes are:- integer , float , string , boolean ,None 
single line command : #This is a command line
multi line command : using 3 ' we can command multiple line

'''


#Printing something

print("Hello world")    # In python we can print something using " " & ' ' & ''' ''' 
print('Hello world')    # Also we can declear the string using same method as above
print('''Hello world''')


#Data Types and veriables

a = 39   #Integer 
b = 130.0   #Floating point number
c = "String"  #String 
d = True    #Boolean
e = None   #None 

print(a,b,c,d,e)  # Print all values of veriables

print(type(a),type(b),type(c),type(d),type(e)) # Print all Date of veriables using " type() " operator



# Arithmetic Operators are : + , - , * , / , % , *= , /= , += , -=

#Comperision Operators  are : == , != , > , >= , < , <= 

#Logical Operators  are : and , or , not 

bool1 = True 
bool2 = False
print(bool1 and bool2)
print(bool1 or bool2)
print(not bool1)



#Input something

name = input("Enter your name: ")    # python will take input everything as a string 
print(name)


#Type Casting

num = input("Enter a number: ") 
print(type(num))
num = int(num)    #type casting of num from string to integer 
print("After type casting",type(num))
print(num + 50)


