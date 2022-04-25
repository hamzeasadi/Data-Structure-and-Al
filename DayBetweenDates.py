import os
import sys
import argparse
from datetime import date


my_parser = argparse.ArgumentParser(description="this parser takes two argument bith date and some end date!!")
my_parser.add_argument('--birth_date', '-bd', action='store', nargs=1, type=str, required=True)
my_parser.add_argument('--end_date', '-ed', action='store', nargs=1, type=str, default=str(date.today()))

daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def nextDay(*date):
    year, month, day = date[0], date[1], date[2]
    if day < 30:
        return year, month, day+1
    elif month < 12 :
        return year, month+1, 1
    else:
        return year+1, 1, 1

def dayBetweenDates(date1, date2):
    days = 0
    while isBefore(date1, date2):
        days+=1
        date1 = nextDay(date1)

    return days

    

def isBefore(date1, date2):
    if date1[0]<date2[0]:
        return True
    elif (date1[0]==date2[0]) and (date1[1]<date2[1]):
        return True
    elif (date1[1]==date2[1]) and (date1[2]<= date2[2]):
        return True
    else:
        return False


def main():
    birthdate = list(map(int, my_parser.parse_args().birth_date[0].split('-')))
    enddate = list(map(int, my_parser.parse_args().end_date.split('-')))
    print(dayBetweenDates(date1=birthdate, date2=enddate))

if __name__ == '__main__':
    main()