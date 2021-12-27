import os
import itertools as it
import random



def multiplierof(n):
    def multiplier(x):
        print(f"{n}x{x} = {n*x}")
    return multiplier



def main():
    n, x = map(eval, input("Please enter n, x: ").strip(' ,').split(','))
    mymul = multiplierof(n)
    mymul(x)




if __name__ == '__main__':
    main()
