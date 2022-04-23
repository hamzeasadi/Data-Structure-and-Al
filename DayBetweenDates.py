import os
import sys
import argparse
from datetime import date

my_parser = argparse.ArgumentParser(description='this arg parser takes two dates in yy-mm--dd format')
my_parser.add_argument('--birthDate', type=str, required=True)
my_parser.add_argument('--endDate', type=str, default=str(date.today()))

def nextDay(*date):
    year, month, day = date[0], date[1], date[3]
    if day<30:
        return year, month, day+1
    elif month < 12:
        return year, month+1, 1
    else:
        return year+1, 1, 1
        



def main():
    pass

if __name__ == '__main__':
    main()