import os
import sys
import argparse
import numpy as np

my_arr = np.random.randint(low=-10, high=10, size=10)

def maxsubarr(*arr):
    size = len(arr)
    msf = -100000
    meh = 0
    for i in range(size):
        meh += arr[i]
        if meh > msf :
            msf = meh
        if meh < 0:
            meh = 0
        
    return meh, msf


def main():
    meh, msf = maxsubarr(*my_arr)
    print(my_arr)
    print(f"meh={meh}, msf = {msf}")


if __name__ == '__main__':
    main()