import datetime
import time


def print_date(a):
    print(f"Текущая дата {a}")


def outher(date):
    def inner(d):
        print("Время выполнения", datetime.datetime.today()-date)
        d(date)
    return inner


outher(datetime.datetime.today())(print_date)
