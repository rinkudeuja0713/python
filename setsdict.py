#set: cannot repeat element like in list and are unchangeable and not ordered
set1 = set()
print(type(set1))

s1= {1,3,5,7}
s2= {2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))

s3={1,2,3,4}
s4={5,6,7}
print(s3.isdisjoint(s4))
print(s4.issubset(s3))
print(s1.isdisjoint(s2))

s4.remove(5)
print(s4)
s4.discard(9)
print(s4)
s6=s3.pop()
print(s6)

# del s2
set123= {"rinku", 22, True,}
if 22 in set123:
    print("correct")
else:
    print("False")

# dictionary
dict = { "Name": "Harry","age":19, "question":True}
print(dict)
print(dict["age"])
print(dict.get("Name"))
print(dict.get("place"))

print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(f"the value for {key} is {dict[key]}")

dict1 = {"first":"social","hours": 2, "valiud": False}
print(dict1.items())
print(dict1.get("name"))
print(dict1["first"])
for key, value in dict1.items():
    print(f" the thing for {key} is {value}")    

e1 = {21:55, 9:70, 24:81}
e2= {22:58}
e1.update(e2)
print(e1)
e1.popitem()
print(e1)
del e1[9]
# e1.clear()


e4= {}
print(type(e4))



# Extras

for i in range(5):
    print(i)
    if i ==3:
        break
else:
    print("no")

for x in range(6):
    print("this is the iteration of {} ".format(x+1))

for x in range(6):
    print(f"This is the iteration of {x+1}")
else:
    print("sorry no")




