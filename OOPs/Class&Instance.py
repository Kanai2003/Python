#in class attribute all details are same for all like company name ,company address etc. but in instance attribute other things are different


class Employee:
    company = "Google"              #class attribute
    eligible = "18+"                #class attribute

Kanai = Employee()
Driptanil = Employee()

print(Kanai.company,Kanai.eligible)
print(Driptanil.company,Driptanil.eligible)

Employee.company = "YouTube"

print(Kanai.company,Kanai.eligible)
print(Driptanil.company,Driptanil.eligible)


Kanai.salery = 2000                 #instance attribute
Driptanil.salery = 2000             #instance attribute

print(f"{Kanai.salery}\n{Driptanil.salery}")         #instance attribute has higher precedence than class attribute during assignment & retrival











