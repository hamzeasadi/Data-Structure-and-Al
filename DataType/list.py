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
        multValu = sum(list(map(lambda x,y:x*y, it.tee(arr, n=2))))
        return multValu

# def evenOdd function







def main():
    # arr = list(map(eval, input("please enter element of an arry, comma seperated:").strip(' ,').split(',')))
    n = int(input("enter array size: "))
    arr = random.choices(range(1, 5), k=n)
    out = listMult(arr)
    print(arr)
    print(out)



if __name__ == '__main__':
    main()
