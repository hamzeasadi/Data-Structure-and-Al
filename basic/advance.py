import os
import itertools as it
import random



def multiplierof(n):
    def multiplier(x):
        print(f"{n}x{x} = {n*x}")
    return multiplier

def my_decorator(func):
    def wrapper():
        print("sth happen before the function is called!!")
        func()
        print("sth happen after the function is called!!")

    return wrapper


@my_decorator
def say_whee():
    print("whee!!")

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twice
def greet(name):
    print(f"Hello {name}")

class Celsius():
    def __init__(self, temp):
        self.__temp = temp

    def to_farenhit(self):
        return self.__temp*1.8 + 32




"""
a decorator function real story is as following
@decorator
def myfunction(): === myfunction = decorator(myfunction)
    ....
"""

def main():

    # say_whee = my_decorator(say_whee)
    # say_w()
    # print(say_w)
    greet(name='asqar')




if __name__ == '__main__':
    main()
