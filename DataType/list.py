import os
import sys
import random
from fractions import Fraction
import math
import cmath
from decimal import Decimal
import itertools as it

random.seed(42)

# def listMult function
def listMult(arr: list):
    """listMult function accept a list and multiply its elements together
    args:
        arr: an arbitrary size list with integers, float or coplex values
    return:
        multValue: return the multiplication of the list elements
    Raises:
        ValueError: if list elements are not a number
    """
    if any(isinstance(item, str) for item in arr):
        raise ValueError(f"Expected all elements to be numbers but Got String type as well")
    else:
        # multValu = it.accumulate(arr, func=lambda x, y: x*y)
        # return list(multValu)[-1]
        # multValu = math.prod(arr)
        # return multValu
        multValu = 1
        for x in arr:
            multValu *= x
        return multValu





# def a shape function for list
def shape(arr: list):
    """this function takes in a list and return it's shape
    args:
        arr: an arbitrary size list
    returns:
        a tuple that shows the list shape
    raises:
        if it's not a list raise TypeError
    """
    n = len(arr)
    if (n>0 and isinstance(arr, list)):
        dim = [n]
        if len(arr[0]>0):
            dim.append(len(arr[0]))
        elif len(arr[0][0])>0:
            dim.append(len(arr[0][0]))
        elif len(arr[0][0][0])>0:
            dim.append(len(arr[0][0][0]))
        elif len(arr[0][0][0][0])>0:
            dim.append(len(arr[0][0][0][0]))
        elif len(arr[0][0][0][0][0])>0:
            dim.append(len(arr[0][0][0][0][0]))
        else:
            return tuple(arr)
    else:
        raise TypeError(f"Expected a list, Got {arr}")







def main():
    # arr = list(map(eval, input("please enter element of an arry, comma seperated:").strip(' ,').split(',')))
    mytuple = ([1, 2, [1, 2]])
    



if __name__ == '__main__':
    main()
