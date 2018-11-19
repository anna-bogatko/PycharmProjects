"""
table
object reference count

"""


a = "nyc"
b = "nyc"

print(a)

a = 123

print(a)
print(b)

b = 456

print(b)

c = "nyc"
d = c

print(d==c)
print(c is d)