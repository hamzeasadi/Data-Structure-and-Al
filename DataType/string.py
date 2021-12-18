import random
import os
import cmath

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
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).ljust(thickness*6))


def main():
    thickness = int(input("please enter thickness: ").strip())
    textAlignment(thickness, 'H')

if __name__ == '__main__':
    main()
