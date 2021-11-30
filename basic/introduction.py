import cmath
import math




# Python Program to Find the Square Root
def Root(x):
    """Find the root of the given value"""
    try:
        x = float(x)
        if isinstance(x, complex) or x<0:
            root_val = cmath.sqrt(x)
            print(f"the root value of given number, {x} is a complex number: {root_val}")
        else:
            root_val = math.sqrt(x)
            print(f"the root value of given number, {x} is a real number: {root_val:.4f}")
    except Exception as e:
        x = complex(x)
        print(f"the input value was an complex number: {x}")
        root_val = cmath.sqrt(x)
        print(f"the root value of given number, {x} is a complex number: {root_val}")








if __name__ == '__main__':
    num = input("please enter a number to calculate the root value: ")
    Root(num)
