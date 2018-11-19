"""
Build-in methods to help manipulate with lists
"""

cars = ["bmw", "honda", "audi"]

length = len(cars)
print(length)

"""
Add item to the end of the list 'cars'
"""
cars.append('Benz')
print(cars)

"""
Add item to the specified place in the list 'cars'
"""
cars.insert(1,'Jeep')
print(cars)

"""
Find the place in the list of some specifies item
"""
x = cars.index("honda")
print(x)

"""
Remove items from the list (from the end of the list)
"""
y = cars.pop()
print(y)
print(cars)

cars.remove("Jeep")
print(cars)

"""
Slice lists
"""
slicing = cars[1:] #gives all items from the list starting from index 1
print(slicing)

"""
slicing = cars[0:2] #gives all items from the list starting from index 0 to 2. 0 is included, 2 is excluded
print(slicing)
"""
slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)
print(cars)

print("*"*30)

"""
Sort list
"""
print(cars)
cars.sort()

print(cars)