# 3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух из них.

def f(*args):
    print(sum(args) - min(args))


f(3,1,2)
