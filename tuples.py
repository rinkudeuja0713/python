# # tuples in python: used for constant list cause it cannot be changed
# tup = (1,3,7, False, "cherry")
# print(type(tup))
# print(len(tup))
# print(tup)
# print(tup[0])
# print(tup[3])

# if 34 in tup:
#     print("yes")
# else:
#     print("no")

# tup1= tup[1:4]
# print(tup1)

countries = ("spain", "nepal", "india", "russia")
temp = list(countries)
temp.append("china")
temp.pop(2)
temp.insert(2,"finland")    #temp[2]="finland"
countries = tuple(temp)
print(countries)
res = countries.count("nepal")
print(res)
res2= countries.index("spain")
print(res2)


coun = ("efr", "rhu", "rkke")
coun2 = ("sdhj","akdjh","skdhwk","skdbsk")
coun3= coun + coun2
print(coun3)


