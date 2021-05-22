import datetime
import time


def funk3(a):
    print(f"Текущая дата {a}")


def func1(date):
    def funk2(d):
        print("Время выполнения", datetime.datetime.today()-date)
        d(date)
    return funk2


func1(datetime.datetime.today())(funk3)