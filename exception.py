x = input("Enter a number: ")
try:
   for i in range (1,11):
    print(f"{int(x)} x {i} ={int(x)*i}")
except:
  print("error")

try:
    y = int(input("enter an integer"))
    num1 = [6,9]
    print(num1[y])
    

except ValueError:
    print("this is not an integer")

except IndexError:
    print("this is index error")


# importance of finally: always executes even with return function
def func():
  try:
    y = int(input("enter an integer"))
    num1 = [6,9,3,5]
    print(num1[y])
    return 1

  except:
    print("this is error")
    return 0
  
  finally:
    print("this is always executed even if theres error or not")

num = func()
print(num)

# raising custom errors in python
y=int(input("enter a number in between 2 and 9"))
if (y<2) or (y>9) :
    raise ValueError(" the value shoud be betn 2 and 9")


 



    




    


    














