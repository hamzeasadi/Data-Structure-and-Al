import os
import sys
import argparse
from datetime import date


my_parser = argparse.ArgumentParser(description="this parser takes two argument bith date and some end date!!")
my_parser.add_argument('--birth_date', '-bd', action='store', nargs=1, type=str, required=True)
my_parser.add_argument('--end_date', '-ed', action='store', nargs=1, type=str, default=str(date.today()))


def main():
    birthdate = my_parser.parse_args().birth_date
    enddate = my_parser.parse_args().end_date
    print(enddate)
    print(birthdate)

if __name__ == '__main__':
    main()