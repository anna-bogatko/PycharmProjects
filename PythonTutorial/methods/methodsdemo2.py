"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

def sum_nums(n1=3, n2=10):
    """
    Get sum of numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

#sum1 = sum_nums(n1=20, n2=30)
sum1 = sum_nums(n1=20)

print(sum1)




