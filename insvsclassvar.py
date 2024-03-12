# instance vs class variable in python
# below: raiseamt is an instance variable while company is class variable

class Employee():
    company="Google"
    def __init__(self,name):
        self.name = name
        self.raiseamt= 0.2
    def Show(self):
        print(f" the employee {self.name} has a raise of {self.raiseamt} in company: {self.company}")

# Employee.company= "fb"
e1= Employee("rohan")
# Employee.Show(e1)
e1.Show()

e2= Employee("shweta")
e2.raiseamt = 0.4
e2.company="Fonepay"
e2.Show()

e3= Employee("sheena")

e3.Show()


