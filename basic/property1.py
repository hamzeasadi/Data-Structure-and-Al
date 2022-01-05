import os
import random

def dotwice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@dotwice
def saySth(a):
    print(f"the positional argument was: {a}")


def main():
    a = input("please enter some warm welcom sentences: ").strip(' ')
    # saysth = dotwice(saySth)
    saySth(a)




if __name__ == '__main__':
    main()
