# string formatting
intro = "Hey my name is {1} and I am from {0}"
name="Rinku"
country="Nepal"
print(intro.format(name, country))
print(intro.format(country, name))
