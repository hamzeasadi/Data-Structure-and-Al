import math
import random
import sys
import os
import cmath
from fractions import Fraction
import numpy as np
import decimal

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
    if not(n>0 and isinstance(n, int)):
        raise ValueError(f"Expected a positive integer, Got {n}")

    for i in range(n):
        for j in range(i+1):
            character = chr(65 + i + j)
            print(f"{character} ", end='')
        print()

# define a function to subtract matrix diognals
def diognalDifference(arr):
    """a function to calculate diognal difference of square matrix
    args:
        arr: the square matrix
    return:
        the absolute difference between diognals
    Raises:
        None
    """
    diognal_1 = 0.0
    diognal_2 = 0.0
    size = len(arr)
    for i in range(size):
        diognal_1 += arr[i][i]
        diognal_2 += arr[i][n-i-1]
    return abs(diognal_1 - diognal_2)



# define a function to print positive, negative, and zero porportion of an array
def PlusMinus(arr: list):
    """ A function to print positive, negative, and zero porportion of an array
    args:
        arr: an arbitrary size array
    return:
        print the positive, negative and zero proportion
    Raises:
        None
    """
    n = len(arr)
    negatives = sum([x<0 for x in arr])/n
    zeros = sum([x==0 for x in arr])/n
    positives = 1 - zero - negatives
    print(f"{negatives:0.6f}\n {zeros:.6f}\n{positives:.6f}")

# define a function to create a staircase of height n and width
def staricase(n: int):
    """ staircase witll take a integere and print out a starcaise of size n*n
    args:
        n: an arbitrary positive integer
    Raises:
        it will raise an value error if an negative number given
    """
    if (n>0 and n<=100):
        x = ' '
        sharp = '#'
        for i in range(1, n):
            t = (n-i)
            print(f"{t*x}{i*sharp}{x}")
        else:
            print(f"{(n)*sharp}")

    else:
        raise ValueError(f"Expected a positive integer, Got {n}")

# define the min max sum function
def MinMaxSum(arr: list):
    """ the min max sum function calculate the summation of four smallest and largest values in given list
    args:
        arr: an arbitrary ary that its size is bigger than 4
    return:
        max4: summation of the 4 largest value in arr
        min4: summation of the 4 smallest value in arr
    Raises:
        None
    """
    arr.sort()
    min4 = sum(arr[:4])
    max4 = sum(arr[-4:])
    print(f"{min4}  {max4} {isinstance(max4, int)}, {sys.getsizeof(max4)}")

# def birthdayCakeCandles function
def birthdayCakeCandles(candles):
    """Function Description
        birthdayCakeCandles takes in a list and print out all max values
        args:
        candles[n]: the candle heights
        Returns:
            int: the number of candles that are tallest
        Input Format:
            The first line contains a single integer, , the size of .
            The second line contains  space-separated integers, where each integer  describes the height of.
        Raises:
        None
    """
    print(f"{candles.count(max(candles))}")


# define timeConversion function
def timeConversion(s):
    """this function convert 12 oclock format time to 24 hour format
    args:
        s: time in 12 hour format
    return:
        time_24h_format: return a string for 24 hour format
    raises:
        None
    """
    s = s.strip()
    AM_PM = s[-2:]
    time_12h = list(map(int, s.rstrip('P, A, M').split(':')))
    if AM_PM == 'AM':
        if time_12h[0] != 12:
            return s[:-2]
        return f"{0}{0}:{s[3:5]}:{s[6:8]}"
    else:
        if time_12h[0] != 12:
            return f"{time_12h[0]+12}:{s[3:5]}:{s[6:8]}"
        return f"{time_12h[0]}:{s[3:5]}:{s[6:8]}"

# define hourglassSum function
def hourglassSum(arr):
    """
    An hourglass in  is a subset of values with indices falling in this pattern in arr's graphical representation:
    a b c
      d
    e f g
    this function find the hourglass and calculate their summation and return the max value
    args:
        arr: an aribitrary n*n matrix
    return:
        hourgloass_max: maximum value related to hourglass
    Raises:
        None
    """
    summations = []

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            x = 0.0
            x += sum(arr[i][j:j+3])
            x += arr[i+1][j+1]
            x + sum(arr[i+2][j:j+3])
            summations.append(x)
    print((summations), max(summations), len(summations))

# define RadianToDegree function
def RadianToDegree(radian):
    """takes radian and convert it to degree
    args:
        radian: an arbitrary number
    return:
        degree: converted value of radian
    Raises:
        None
    """
    return (radian/math.pi)*180

# define floatDecimal function
def floatDecimal(x, y):
    """ floatDecimal function takes two numbers and return their summation based on floating operator and decimal operator
    args:
        x, y: two arbitrary numbers
    return:
        None
    print:
        print the summation of two number based on decimal package and normal float operation
    Raises:
        None
    """
    sum_d = decimal.Decimal(x) + decimal.Decimal(y)
    sum_f = x+y
    print(f"sum_d={sum_d}, sum_f={sum_f}, {sum_f==sum_d}")
    print(Fraction(sum_f))

# define a function to append or extend a list
def appExt(mylist: list, *x):
    """ appExt function based on the lenght of x execute append or extend on mylist
    args:
        mylist: a arbitray size list
        x: an arbitray variablenumber of element to add to list
    Returns:
        my_extended_list: return the new created list
    Raises:
        None
    """
    if len(x) < 2:
        mylist.append(x[0])
    else:
        mylist.extend(list(x))
    return mylist

# define myInsert function
def myInsert(arr: list, *items, idx, use_insert=False):
    """ myInsert takes in a list and insert items in idx position
    args:
        arr: an arbitray size list
        items: items that require to add to the list
        idx: index which we add the items
        use_insert: if it's true we use insert built-in function
    Returns:
        return the new list
    Raises:
        ValueError is idx is out ot range
    """
    if idx < len(arr):
        if use_insert:
            arr.insert(idx, list(items))
        else:
            arr[idx:idx] = list(items)
        return arr
    else:
        raise IndexError(f"Expected index size less than {len(arr)}, Got {idx}")




random.seed(42)

if __name__ == '__main__':
    n = int(input("input an integer number that is the size of list: ").strip())
    arr = random.choices(population=range(1, 10), k=n)
    new_arr = myInsert(arr)
