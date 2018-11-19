"""
Examples to show available string methods in python
"""

#Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC', 1))

#Sub-Strings
# starting index is inclusive
# ending index is exclusive
sub = a[1:6]
#"берет каждую вторую букву"
step = a[1:6:2]

print("XXXXXXXXXXXXXXXXXX")
print(sub)
print(step)