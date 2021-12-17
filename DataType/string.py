import random
import os
import cmath

def count(string: str, character):
    cnt = 0
    for x in string:
        if x==character:
            cnt+=1
    return cnt



def main():
    mystr = 'pycharm'
    del mystr
    print(mystr)


if __name__ == '__main__':
    main()
