"""
Object Oriented Programming
"""

class Car(object):

    #Method __init__ allows to use all attributes, methods for object
    def __init__(self, make, model="550i"):
        self.make_car = make
        self.model_of_car = model

#c1 is outside the class
c1 = Car('bmw')
print(c1.make_car)
print(c1.model_of_car)

c2 = Car('subaru')
print(c2.make_car)
print(c2.model_of_car)