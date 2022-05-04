import os
import sys
import argparse



# factorial functions
def simple_factorial(n):
    if n<=1:
        return 1
    else:
        return n*simple_factorial(n-1)


def main():
    my_parser = argparse.ArgumentParser(description="this parser is used to factorial function")
    my_parser.add_argument('--number', '-n', required=True, default=1, type=int, action='store', nargs=1, help='integer value for calculating factorial')
    n = my_parser.parse_args().number[0]
    recurison_limit = sys.getrecursionlimit()
    if recurison_limit < n:
        sys.setrecursionlimit(n+1)
    factorial = simple_factorial(n)
    print(f"{n}! = {factorial}")



if __name__ == '__main__':
    main()