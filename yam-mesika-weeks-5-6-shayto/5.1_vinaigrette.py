import random
import time
import datetime

MONDAY = 1


def vinaigrette():
    """
     Main function for vinaigrette code
    :return:
    """
    start_date = read_date("Please enter start date in YYYY-MM-DD format: ")  # get first date
    end_date = read_date("Please enter end date in YYYY-MM-DD format: ")  # get second date
    rand_date = random_date(start_date, end_date, '%Y-%m-%d', random.random())  # generate random date
    print(rand_date)
    if check_if_monday(rand_date):  # check if date is monday and if yes print "אין לי ויניגרט"
        print("אין לי ויניגרט")


def read_date(string):
    """
     function to get date from user. gets an str and returns date.
    :param string: date
    :return: date
    """
    user_date_input = input(string)
    return user_date_input


def random_date(start_date, end_date, time_format, prop):
    """
     function to generate random date.
    :param start_date:beginning of range
    :param end_date:end of range
    :param time_format:YYYY-MM-DD
    :param prop:proportion of a range
    :return:random date in range
    """
    start_time = time.mktime(time.strptime(start_date, time_format))
    end_time = time.mktime(time.strptime(end_date, time_format))
    ptime = start_time + prop * (end_time - start_time)

    return datetime.date(time.localtime(ptime).tm_year,
                         time.localtime(ptime).tm_mon,
                         time.localtime(ptime).tm_mday)


def check_if_monday(date):
    """
    function gets random date and checks if it falls on a monday.
    :param date: random date in range
    :return: boolean if date falls on monday.
    """
    return date.isoweekday() == MONDAY


if __name__ == '__main__':
    vinaigrette()
