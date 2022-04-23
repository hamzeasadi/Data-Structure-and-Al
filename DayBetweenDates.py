import os
import sys
import argparse
from datetime import date

my_parser = argparse.ArgumentParser(description='this arg parser takes two dates in yy-mm--dd format')
my_parser.add_argument('--birthDate', type=str, required=True)
my_parser.add_argument('--endDate', type=str, default=str(date.today()))

dates = vars(my_parser.parse_args())

print(dates)
print(date.today())




def main():
    pass

if __name__ == '__main__':
    main()