class Employee :
    company = "Google"
    def getSalery(self,Pass_argument):          #self is a parameter which will call object & we can pass a new arguments
        print(f"Salery for this employee working in {self.company} is {self.salery}\n{Pass_argument}")

    @staticmethod       #"@staticmethod" is use to run code like "Employee.greeting()" not like "Employee.greeting(Kanai)"
    def greeting():     #for "@staticmethod" we don't need to use "self" in this method
        print("Good Morning , Mr.Coder")


Kanai = Employee()
Kanai.salery = "200k"
Kanai.getSalery("Thanks :)")          # "Kanai.getSalery" and "Employee.getSalery(Kanai)"
#Employee.salery(Kanai)      #"Kanai.getSalery" is better way to write the code

Kanai.greeting()        # by Using "@staticmethod" we don't need to use "self" or any other passing arguments in method





