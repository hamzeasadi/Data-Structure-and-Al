import os
import math
import random
import numpy as np



def findPoint(px, py, qx, qy):
    r = [2*qx-px, 2*qy-py]
    return r

# define maximumDraws function
def maximumDraws():
    pass

# define handshake
def handshake(n):
    """if we have n people how many hand shakes it is gonna be if
    they handshake each other just ones
    args:
        n: number of people
    returns:
        hs: number of handshakes
    """
    return int((n*(n-1))/2)

def lowestTriangle(a, b):
    """given triangle area (a) and it's base (b) find smallest height(h)
    args:
        a, b: int
    return:
        h
    """
    return int(math.ceil((2*a)/b))

def emailVal(s):
    valid = False
    spart = s.partition('@')
    extpart = s.partition('.')
    if spart[1] == '@':
        if spart[0].isalnum() and spart[2].isalnum():
            if len(extpart[2])<=3 and extpart[2].isalpha():
                return



    return valid

def s(n):
    for i in range(1, n):
        x = map(str, list(range(1, i)))
        x = ''.join(x)
        print(x)



class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueLargeError(Error):
    pass

n = random.randint(0, 1000)

def geusNumber(n):
    mygues = False
    while not mygues:
        try:
            gues = int(input("Enter a number: ").strip())
            if gues>n:
                raise ValueLargeError()
            elif gues< n:
                raise ValueTooSmallError
        except ValueTooSmallError as e:
            print("This value is too small, try again!\n")
        except ValueLargeError as e:
            print("This value is too large, try again!\n")
        else:
            print("Congratulations! You guessed it correctly.")
            mygues = True


def main():
    geusNumber(n)



if __name__ == '__main__':
    main()
