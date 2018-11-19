"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
#Strings for loop
my_string = 'abcabc'

for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

print('*' * 20)

#List for loops
cars = ['bmw', 'benz', 'honda']

for car in cars:
    print(car)


nums = [1, 2, 3]
for n in nums:
    print(n * 10)

print('*' * 30)

#Dictionary for loop
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k + " " + str(d[k])) # We access the key from the dictionary by using str(d[k])

print("*" * 30)

for k,v in d.items():
    print(k)
    print(v)



