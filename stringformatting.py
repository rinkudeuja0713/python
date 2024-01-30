#fstrings /formatting
# letter = "Hey my name is {} and I am from {}"
# country= "India"
# name="Harry"

# print(letter.format(name,country))

name="rinku"
country="nepal"
print(f"Hey my name is {name} and i am from {country} ")

# item= "Only for {} !!!"
# price= 4.099999999
# print(item.format(price))

price = 4.099999
print(f"Only for {price:.2f}")

print(type(f"{2*3}"))
print(f"{2*3:.3f}")


#docstrings/ pep-8: python enhancement proposal: doc that maintain readable python code
def area(b,h):
    ''' Gives the area of a triangle with base b and height h
    '''
    print("The area is ",0.5*b*h)

area(2,4)

print(area.__doc__)

