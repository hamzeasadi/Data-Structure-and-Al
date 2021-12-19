import os
import math
from faker import Faker








def main():
    fake = Faker()
    dictionary = open('list.py', mode='r', encoding='utf-8')
    print(dir(dictionary))
    for line in dictionary.readlines():
        print(line)

if __name__ == '__main__':
    main()
