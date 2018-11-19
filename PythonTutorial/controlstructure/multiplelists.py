"""
Iterating multiple lists at the same time
"""

l1 = [1, 2, 3]
l2 = [5, 6, 7, 30, 40 ,50]

for a,b in zip(l1, l2):
    print(a)
    print(b)

print('#' * 40)

for a,b in zip(l1, l2):
    if a < b:
        print(a)
    else:
        print(b)




