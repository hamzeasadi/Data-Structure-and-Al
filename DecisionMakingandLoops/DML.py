import math
import random
import sys
import os
import cmath
from fractions import Fraction
# import keyword
# print(help(keyword))
# print(keyword.__doc__)


def range_test(range_vars):
    start, stop, step = range_vars.split(',')
    start, stop, step = eval(start), eval(stop), eval(step)
    range_obj = range(start, stop, step)
    range_list = list(range_obj)
    print(f"the range object is: {range_obj}")
    print(f"list(range_obj): {range_list}")
    # print(f"dir(range_obj): {dir(range_obj)}")
    range_obj_attr = dir(range_obj)
    if '__next__' in range_obj_attr:
        print(f"range_obj is an iterator")
    elif '__iter__' in range_obj_attr:
        print(f"range_obj is an iterable")
    else:
        print("range_obj is not an iterable and iterator")

def factorial(n):
    """ This function compute the factorial of the input number
    args:
        n: it should be a natural number or zero
    return:
        it will return the factorial of the input number
    exception:
        it will raise error if the given number is not natural or zero

    """
    if isinstance(n, int) and n>=0:
        if n<1:
            return 1
        else:
            return factorial(n-1)*n

    else:
        raise ValueError

# check positivity of a number
def signCheck(x):
    """sign check function, it will check if a number is positive , negative, or zero
    args:
        an aribitray number
    return:
        the sign of given n umber
    exception:
        no error handling
    """
    x = eval(x)
    if x>0:
        print(f"{x} is positive")
    elif x<0:
        print(f"{x} is negative")
    else:
        print(f"{x} is zero")

# check if the number is even or not
def iseven(x):
    """check if the number is even or not
    args:
        a arbitrary number as input
    return:
        print the result of check the function
    Raises:
        not any exception araised
    """
    x = eval(x)
    if x%2==0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")




if __name__ == '__main__':
    print(signCheck.__doc__)
    num = input("please enter a number to compute its sign: ")
    signCheck(num)
