a = "1"
b = "2"
print(a+b)
# explicit type casting
print(int(a)+int(b))

# implicit type casting
c = 1.9
d = 8
print(c+d)

name = "rinku"
print(name[0])
description = ''' hey,
i am from bhaktapur
i like "apple"
'''
for character in name:
    print(character)
for character in description:
    print(character)
namelist = "haresh,ram,sikar"
print(len(namelist))
print(namelist[0:4])
print(namelist[-3:-1])


# strings are immutable: cannot be changed but makes a new string when calling upper or lower
example = "Ramila!!!! !!! !!"
print(len(example))
print(example.upper())
print(example.lower())
print(example.rstrip('!'))
print(example.replace("Ramila","John"))
print(example.split(" "))
heading= "introduction to hTml1"
print(heading.capitalize())
print(heading.center(50))
print(example.count("Ramila"))
print(example.count("!"))
print(example.endswith("!",3, 8))
print(heading.find("to"))

# alphanumeric: string incl a-z, A-Z, 0-9 
alnumeg = "helloWolrd"
print(alnumeg.isalnum())
print(alnumeg.isalpha())
print(alnumeg.islower())
print(heading.isprintable()) 
#\n is not printable character
print(alnumeg.isspace())
#true if theres white space using keyboard in the string
print(alnumeg.istitle())
#true if fist charcter is capital
print(heading.startswith("introduction"))
print(alnumeg.title())



