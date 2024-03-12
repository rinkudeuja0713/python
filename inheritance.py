class Employee():
    def __init__(self,name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"the employee:{self.id} is {self.name}")

class Programmer(Employee):
    def ShowText(self):
        print("this is python for beginners")
    
e1=Employee("sujata", 201)
e1.show()
e2=Programmer("rahul", 125)
e2.show()
e2.ShowText()

# # access specifiers/modifiers

# class Student():
#     def __init__(self,name,age):
#         self.__name= name
#         self.__age= age
#     def __show(self):
#         print(f"{self.name} , {self.age}")

# a= Student("rita", 22)
# print(a._Student__name)

