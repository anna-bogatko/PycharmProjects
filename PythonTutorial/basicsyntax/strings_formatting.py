"""
Examples to show how strings formatting works in python
"""

city = 'nyc'
event = 'show'

print("Welcome to " + city + " and enjoy the " + event)

print("Welcome to %s and enjoy the %s" % (city, event))
print("Welcome to %s" % city)

