import os
import math
import random




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
    return (2*a)/b



def main():
    pass



if __name__ == '__main__':
    main()
