# lists: ordered collection of data items and can be changed

l = [3,5,4," rinku", True]
print(type(l))
print(l)
print(l[1])
print(l[1:])
print(l[1:6:2])
l.insert(1,21)
print(l)


l.append(7)
print(l)
print(l.count(3))

m = l.copy()
m[0]=1
print(m)
print(l)





if 7 in l:
    print("yes")
else:
    print("no")
if "ink" in "rinku":
    print("YES")
else:
    print("no")

list1 = [i for i in range(5)]
print(list1)
list2 = [i for i in range(5) if i%2==0]
print(list2)

list1.extend(m)
print(list1)


