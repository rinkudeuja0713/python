age=int(input("enter your age: "))
print("your age is: ",age)

if age>=18:
    print("you can vote")
else:
    print("you cannot vote")

# # match-case statements: like switch case statements
x =int(input("enter the value for x"))
match x:
    case 0:
        print("x is zero")
    case 2:
        print("x is two")
    case _:
        print(x)

# loops in python: for 
name = "Abhishek"
for i in name:
    print(i)
    if(i == "b"):
        print("found it!!!")

colors=["green","bkue","red"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for num in range(1,88):
    print(num)
for num1 in range(1,12,2):
    print(num1)

#loops in python: while
il = 0
while (il<=5):
    print(il)
    il=il+1
print("that was a while loop")

im=0
while(im<=12):
    im = int(input("enter a number: "))
    print(im)

count = 5
while(count>0):
    print(count)
    count= count -1
else:
    print("this is else")

# emulate do-while loop

# # short hand if-else statement
# a = 3300
# b = 333
# print("A") if a>b else print("=") if a==b else print("B")

# c=9
# print(c)if a>b else ""
    




    



