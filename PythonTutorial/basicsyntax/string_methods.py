"""
Examples to show available string methods in python
"""

# Accesssing characters in a string
# index starts from zero 0
first = "nyc"[2]
city = "sfo"
print(first)
ft = city[0]
print(ft)


"""
len()
lower()
upper()
stri()
"""

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))
print(stri + str(2))


"""
Concatenation
"""
print("Hello " + " " + " World !!!")
print(first + " " + city)