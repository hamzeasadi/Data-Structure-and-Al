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
    dim = []
    try:
        n = len(arr)
        if n>0 :
            dim.append(n)
            if len(arr[0])>0:
                dim.append(len(arr[0]))
                # print(dim)
                if len(arr[0][0])>0:
                    dim.append(len(arr[0][0]))
                    if len(arr[0][0][0])>0:
                        dim.append(len(arr[0][0][0]))
                        if len(arr[0][0][0][0])>0:
                            dim.append(len(arr[0][0][0][0]))
                    # print(dim)
    except Exception as e:
        # print()
        return tuple(dim)


def runner_up_score(arr):
    arr.sort(reverse=True)
    temp = max(arr)
    for i in arr:
        if i<temp:
            temp=i
            break
    print(temp)

def nestedlist(arr):
    arrnew = list(arr[0])
    arrnew.sort()
    temp = min(arrnew)
    for i in arrnew:
        if i>temp:
            temp=i
            break
    indc = [i for i, x in enumerate(arr[0]) if x==temp]


def merge_the_tools(string, k):
    t = int(len(string)/k)
    for i in range(t):
        block_t = set(string[i*k:k*(i+1)])
        block_idx = [list(string[i*k:k*(i+1)]).index(x) for x in block_t ]
        block_idx.sort()
        out = [string[i*k:k*(i+1)][x] for x in block_idx]
        print(''.join(out))

def poly_check():
    x, k = list(map(int, input().strip().split()))
    poly_eq = input().strip()
    exec(f'print(k == {poly_eq})')

def TriangleQuest(N):
    for i in range(1, N):
        print(((10**i)//9)**2)

def AngleMBC(AB, BC):
    degree_sign = u"\N{DEGREE SIGN}"
    theta = math.atan2(AB, BC)*180/math.pi
    print(fr'{round(theta)}{degree_sign}')

def ModDivmod(a, b):
    # import division from __future__
    print(a//b)
    print(a%b)
    print(divmod(a, b))


def main():
    ModDivmod(177, 10)





if __name__ == '__main__':
    main()
