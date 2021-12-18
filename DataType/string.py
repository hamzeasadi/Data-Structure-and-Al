import random
import os
import cmath
import textwrap

def count_substring(string, sub_string):
    string = string.strip()
    sub_string = sub_string.strip()
    cnt = 0
    ls = len(string)
    lss = len(sub_string)
    for i in range(ls):
        if string[i:lss+i] == sub_string:
            cnt += 1

def textAlignment(thickness, c):
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


def wrap(string, max_width):
    string += '\n'
    output = textwrap.wrap(text=string, width=max_width)
    output = '\n'.join(output)
    return output

def coordinate(x, y, z, n):
    x = set([(i,) for i in range(x)])
    y = set([(i,) for i in range(y)])
    z = set([(i,) for i in range(z)])
    allset = x.union(y.union(z))
    print(list(allset))

def Prob(a, b, c):
    h = min(c, a)
    w = min(c, b)
    return (0.5*h*w)/(a*b)


def main():
    a, b, c = list(map(int, input("a, b, c: ").strip().split(',')))

    print(Prob(a,b,c))




if __name__ == '__main__':
    main()
