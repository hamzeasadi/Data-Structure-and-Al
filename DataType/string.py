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



def main():
    string, substring = input("please enter string, substring: ").strip().split(',')
    string = string.strip()
    substring = substring.strip()
    print(f"{string}, {substring}")
    Count(string, substring)
if __name__ == '__main__':
    main()
