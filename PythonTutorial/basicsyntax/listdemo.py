"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

cars = ["bmw", "honda", "audi"]
empty_list = []
print(cars)
print(empty_list)

print("@#"*20)

print(cars[1])


num_list = [1, 2, 3]
sum_numerous = num_list[0] + num_list[1]

print(sum_numerous)


more_cars = ["bmw", "honda", "audi"]
print(more_cars[2])

more_cars[2] = 'Benz'

print(more_cars[2])
print(more_cars)
