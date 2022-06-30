# 1. creat a class programmer for storing information of few programmer working at Microsoft

# class Programmer :
#     company = "Microsoft"
#     Branch = "India"
#     def __init__(self,name, salery , qualification):
#         self.name = name
#         self.salery = salery
#         self.qualification = qualification
#     def getInfo(self):
#         print(f"Company Name : {self.company}\nBranch : {self.Branch}")
#         print(f"Details of Programmer :\n\tName : {self.name}\n\tSalery : {self.salery}\n\tQualification : {self.qualification}\n")



# Kanai = Programmer("Kanai","200k","B.Tech")
# Ritam = Programmer("Ritam","200k","B.Tech")
# Driptanil = Programmer("Driptanil","250k","B.Tech")

# Kanai.getInfo()
# Ritam.getInfo()
# Driptanil.getInfo()



# --------------------------------------------------------------------------------------------
# 2. Write a class Calculator capable of finding Squre , Qube and Squre-root of a number with a staticmethod greeting 

# class Calculator:
#     def __init__(self,num): 
#         self.number = num

#     @staticmethod
#     def greet():
#         print("Hello")

#     def Squre(self):
#         print(f"Squre of {self.number} is {self.number*self.number}")

#     def Qube(self):
#         print(f"Qube of {self.number} is {self.number**3}")

#     def SqureRoot(self):
#         print(f"Squre root of {self.number} is {self.number**.5}")



# num  = int(input("Enter a number : "))
# a = Calculator(num)
# a.greet()
# a.Squre()
# a.Qube()
# a.SqureRoot()


# -------------------------------------------------------------------------------------
# 3. Write a class Train which has methods to book a ticket , get status(no of seats) and get fare information of a train 

from code import interact


class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Name of the Train is {self.name} and available seat  {self.seats} and The price of the Train is {self.fare}")


    def bookTicket(self):
        if(self.seats >= 1):
            print(f"Your ticket has been booked! \nYour Ticket no is : {self.seats}\nHappy Journey :)")
            self.seats -= 1
        else:
            print("Sorry , This Train is boocked! \n kindly try in tatkal")


interstate = Train("Interstate Express ",75,300)

interstate.getStatus()
interstate.bookTicket()

interstate.getStatus()
interstate.bookTicket()

interstate.getStatus()
interstate.bookTicket()



# -----------------------------------------------------------------------------------
# Can we change "self" in methods ? ->Yes we can. let's do it 
class Sample:
    def __init__(sf,name):
        sf.name = name

obj = Sample("Kanai")
print(obj.name)

