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








if __name__ == '__main__':
    num = eval(input("please enter a number to compute its factorial: "))
    fact_n = factorial(num)
    print(f"the factorial of {num} is {fact_n}")
