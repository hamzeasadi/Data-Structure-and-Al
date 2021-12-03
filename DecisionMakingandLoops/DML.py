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

# check leap year
def isLeap(year):
    """this function simply check if a given year is leap or not
    args:
        year: its a integer value
    return:
        print True if it's a leap year
    Raise:
        this function raise an error if the given value is not int
    """
    if isinstance(year, int):
        if year%4==0 and year%100 !=0:
            print(f"{year} is a leap year")
        elif year%400 ==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        raise TypeError

# Python Program to Find the Largest Among Three Numbers
def maxof3(*numbers):
    """find the maximum number in 3 numbers
    args:
        3 float or int number
    return:
        it will return the lagest value of the 3 numbers
    Raises:

    """
    my_max = numbers[0]
    if numbers[1]>my_max:
        my_max = numbers[1]
    elif numbers[2]>my_max:
        my_max = numbers[2]
    return my_max

# check if a number is prime
def primeCheck(n: int):
    """this function checks if a number is prime
    args:
        an integer number
    return:
        if input number is prime it will return True otherwise False
    Raises:
        None
    """
    root_n = math.sqrt(n)
    if n<=3:
        return n>1
    if n%2==0 or n%3==0:
        return False
    i=5
    while i< n:
        if n%i==0 or (n+1)%i==0:
            return False
        i += 6

    return True


# implement factorial computing
def factorial(n: int):
    """this function gets an positive integer number a returns its factorial
    args:
        n: an positive integer variable
    return:
        n!: it will return the factorial of n (n!=n*(n-1)...2*1)
    Raises:
        It will raise an value error if n>100
    """
    if n > -1 and n < 101:
        if n == 0 :
            return 1
        else:
            return factorial(n-1)*n
    else:
        raise ValueError

# implement a simple function to compute the fibonaci series
def simpleFibo(n:int):
    """This is a simple implementation of fibonaci series computing function
    args:
        n: an positive ingteger number
    return:
        a(n): fibonaci series value at that step (a(n)= a(n-1) + a(n-2)
    Raises:
        raise an error if the given number is less than zero
    """
    if n > -1:
        if n < 2:
            return 1
        else:
            return simpleFibo(n-1) + simpleFibo(n-2)
    else:
        raise ValueError

# implement fibonacci sequence efficiently
cache = {0:1, 1:1}
def fibonacci(n: int):
    """this is a more efficient way of implementing fibonacci sequence in python
    arg:
        n: a positive integer
    return:
        a(n): fibonaccie squence at point n (a(n) = a(n-1)+a(n-2))
    Raises:
        raise an value error if the number is less than zero
    """
    if n>-1:
        if n in cache.keys():
            return 1
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    else:
        raise ValueError(f"positive integer expected, got {n}")

class FiboClass:
    """this class is a blueprint for fibonacci series calculation
        arg:
            n: positive integer variable
        return:
            a(n): fibonacci value at position n --> a(n) = a(n-1) + a(n-2)
        raises:
            Raise an erro if n is negative
    """
    def __init__(self):
        self.cache = {0:1, 1:1}

    def __call__(self, n):
        if n < 0 or (not isinstance(n, int)):
            raise ValueError(f"Except a positive integer, Got {n}")
        if n < len(self.cache):
            return self.cache[n]
        self.cache[n] = self(n-1) + self(n-2)
        return self.cache[n]

# check armstrong number of n digits
def Armstrong(num):
    """ get an n digit number as input and check if it is an armstrong number
    args:
        n: positive integer
    return:
        bool: a boolean number the shows a given number is armstrong or not
    Raises:
        raise a value error if the given number is not a positive integer
    """
    if not (num>1 and isinstance(num, int)):
        raise ValueError(f"Expected a positive integer, Got {num}")
    else:
        n = len(str(num))
        temp = num
        sum = 0.
        while num != 0:
            sum += (num%10)**n
            num = num //10
        return (sum == temp)

# define a pyramid
def pyramid(n):
    """generate a pyramid with n row of stars
    args:
        n: number of rows that build the pyramid
    return:
        print out the pyramid
    Raises:
        ValueError: if n is not a positive integer
    """
    for i in range(n):
        for j in range(n+1):
            print("*", end='')


if __name__ == '__main__':
    # arms = eval(input("please enter the positive integer value: "))
    # arms_ck = Armstrong(arms)
    numbers = list(range(10, int(1e+5), 1))
    arms_check = filter(Armstrong, numbers)
    # print(f"{arms} armstrong check: {arms_ck}")
    print(list(arms_check))
