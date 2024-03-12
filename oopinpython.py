class Person():
    name = "Ram"
    age= 20
    work = "footballer"
    def info(self):
        print(f"{self.name} is {self.age} years old and works as a {self.work}")

a= Person()
b= Person()
a.name = "Charlie"
a.age = 23
a.work = "Painter"

b.name= "Brinda"
b.age= 24
b.work = "Lawyer"

print(a.name, a.age, a.work)
a.info()
print(b.name, b.age, b.work)
b.info()


# constructor is automatically called when an obj of a class is created
# default constructor only has self and no other arguments

class Student():
    def __init__(self, name, age, work):
        self.name = "Stella"
        self.age = 23
        self.work = "dancer"
    def info(self):
        print(f"I am {self.name} and i am {self.age} and work as a {self.work}")

a=Student("Sheela", 20,"nurse")
a.info()


# decorators in python
def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thank you. goodbye")
    return mfx

@greet
def hello():
    print("hello world")

hello()

def add(x,y):
     print(x+y)

greet(add)(1,2)


# another example of using decorator in logging


# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a, b):
#     return a + b





