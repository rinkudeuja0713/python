# there are built in and user defined functions
# defining functions to reduce redundancy of code in python

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("first num is greater")
    else:
        print("second num is greater")

a=9
b=2
c=3
d=2

calculateGmean(a,b)
isGreater(a,b)
calculateGmean(c,d)
isGreater(c,d)

def CalcArea(a,b):
    pass

def name(fname, mname="sen", lname="ghimire"):
    print("hello", fname, mname, lname)

name(" peter"," kris","shah")


# tuples used as an argument in user-defined function
def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum/(len(numbers))

c = average(1,2,3)
print(c)

#dicitonary used as an argument in user-defined function
def name(**name):
    print("Hello, ",name["fname"], name["mname"], name["lname"])

name(fname="ram", mname= "kris" ,lname= "shrestha")
name(fname="rita", mname="prasad", lname="thapa")
