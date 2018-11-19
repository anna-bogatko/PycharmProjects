"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

print(list(range(0, 10)))

a = range(0, 20, 6) #it takes every 6 number from the range
print(a)
print(type(a))

print(list(a))


l = [1, 2, 3]


for num in range(1, 4):
    print(l)