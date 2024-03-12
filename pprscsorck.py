
# Write a python program to create a paper scissior rock game in Python using if-else statements. 
# Do not create any fancy GUI. Use proper functions to check for win.
import random 

def check(comp,user):
    if(comp==user):
        return 0
    if(comp==0 and user==2):
        return -1
    if(comp==1 and user==0):
        return -1
    if(comp==2 and user==1):
        return -1
    else:
        return 1
    
comp = random.randint(0,2)
user = int(input("type 0 for rock, 1 for paper and 2 for scissor  \n"))
print("you: ", user)
print("Computer: ", comp)


output= check(comp, user)
if(output==0):
    print("it's a draw")
elif(output==-1):
    print("You lose")
else:
    print("You've won!")
