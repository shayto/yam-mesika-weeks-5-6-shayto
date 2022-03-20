import random
import time
import datetime

INPUT_DATE_MESSAGE_1 = "Please enter start date in YYYY-MM-DD format: "
INPUT_DATE_MESSAGE_2 = "Please enter end date in YYYY-MM-DD format: "
MONDAY_MESSAGE = "אין לי ויניגרט"
MONDAY = 1


def vinaigrette():
    # main function for vinaigrette code
    start_date = read_date(INPUT_DATE_MESSAGE_1)  # get first date
    end_date = read_date(INPUT_DATE_MESSAGE_2)  # get second date
    rand_date = random_date(start_date, end_date, '%Y-%m-%d', random.random())  # generate random date
    print(rand_date)
    if check_if_monday(rand_date):  # check if date is monday and if yes print "אין לי ויניגרט"
        print(MONDAY_MESSAGE)


def read_date(string):
    # function to get date from user. gets an str and returns date.
    in_date = input(string)
    return in_date


def random_date(start, end, time_format, prop):
    # function to generate random date. gets start- beginning of range
    # end - end of range, time_format, prop- proportion of a range
    # returns random date in range
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)

    return datetime.date(time.localtime(ptime).tm_year,
                         time.localtime(ptime).tm_mon,
                         time.localtime(ptime).tm_mday)


def check_if_monday(date):
    # function gets random date and checks if it falls on a monday returns boolean
    return date.isoweekday() == MONDAY


if __name__ == '__main__':
    vinaigrette()
