class Employee :
   
    company = "Google"


    def __init__(self,name,salery,subUnit):             #"__init__()" is called as constructor method
        print("Employee constructor created")       #for "self" we don't need to call this , it will automatically initialize and run 
        self.name = name
        self.salery = salery
        self.subUnit = subUnit

    def getDetails(self):
        print("Employee details :")
        print("\tcompany : " + self.company)
        print("\tname : " + self.name)
        print("\tsalery : " + self.salery)      
        print("\tsubUnit : " + self.subUnit) 


    @staticmethod       
    def greeting():     
        print("Welcome , Mr.Coder")




Kanai = Employee("Kanai","100k","YouTube")
Kanai.greeting()
Kanai.getDetails()


