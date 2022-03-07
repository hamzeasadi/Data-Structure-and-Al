import os
import math


def wordCount(sentence):
    x = sentence.strip().count(' ') + 1
    print(x)

def coneVolume(r, h):
    volume = 3.14*r**2*(h/3)
    print(volume)

def main():
    r = input().strip()
    h = input().strip()
    r, h = eval(r), eval(h)
    coneVolume(r, h)


if __name__ == '__main__':
    main()
