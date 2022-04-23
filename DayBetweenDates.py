import os
import sys
import argparse
from datetime import date

my_parser = argparse.ArgumentParser(description='this arg parser takes two dates in yy-mm--dd format')
my_parser.add_argument('--birthDate', type=str, required=True)
my_parser.add_argument('--endDate', type=str, default=str(date.today()))

def nextDay(*date):
    year, month, day = date[0], date[1], date[2]
    if day<30:
        return year, month, day+1
    elif month < 12:
        return year, month+1, 1
    else:
        return year+1, 1, 1


def Daysbetweendates(date1, date2):
    print(date1)
    year1, month1, day1 = date1[0], date1[1], date1[2] 
    year2, month2, day2 = date2[0], date2[1], date2[2]
    days = 0
    while ((year2 != year1) or (month1 != month2) or (day1 != day2)):
        year1, month1, day1 = nextDay(*date1)
        days += 1
    return days


def main():
    dates = vars(my_parser.parse_args())
    date1 = list(map(int, dates['birthDate'].split('-')))
    date2 = list(map(int, dates['endDate'].split('-')))
    days = Daysbetweendates(date1=date1, date2=date2)
    print(days)

if __name__ == '__main__':
    main()