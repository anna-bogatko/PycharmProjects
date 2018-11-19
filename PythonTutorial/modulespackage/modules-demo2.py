"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
#import modulesexternal.car as car
#from modulesexternal import car
from modulesexternal.car import info

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        #car.info(make, model)
        info(make, model)

m = ModulesDemo()
m.car_description()
