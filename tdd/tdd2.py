import datetime


def add_five(number):
    return number + 5


def my_min(num_array):
    if len(num_array) == 0:
        return None
    min_num = num_array[0]
    for num in num_array:
        if num < min_num:
            min_num = num

    return min_num


def my_max(num_array):
    if len(num_array) == 0:
        return None
    max_num = num_array[0]
    for num in num_array:
        if num > max_num:
            max_num = num

    return max_num


def has_string(str_array, value):
    the_strings = []
    for current_string in str_array:
        if value in current_string:
            the_strings.append(current_string)

    return the_strings


def to_date(date):
    formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return formatted_date


def date_diff(date1, date2):
    d1 = to_date(date1)
    d2 = to_date(date2)
    return abs(d1 - d2).days


def days_from_end(date):
    formatted_date = to_date(date)
    epoch = datetime.datetime(2012, 12, 21)
    days = (epoch - formatted_date).days

    return days

def contains(value_list, value):
    if value in value_list:
        return True

def add_contents(value_list):
    number = 0
    for value in value_list:
        number += value
    return number

def lookup(value_dict, value_index):
    mine = ' mine'
    if contains(value_dict, value_index):
        return value_dict[value_index] + mine
    else:
        return mine

