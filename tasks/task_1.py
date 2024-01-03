#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def recursion_factorial(n):
    """Рекурсивный алгоритм вычисления факториала."""

    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n - 1)


def recursion_fib(n):
    """Рекурсивный алгоритм вычисление числа Фибоначчи."""

    if 1 >= n >= 0:
        return n
    else:
        return recursion_fib(n - 2) + recursion_fib(n - 1)


def iterative_factorial(n):
    """Итеративный алгоритм вычисления факториала."""

    value = 1
    while n > 1:
        value *= n
        n -= 1
    return value


def iterative_fib(n):
    """Итеративный алгоритм вычисления числа Фибоначчи."""

    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


@lru_cache
def recursion_factorial_lru(n):
    """
    Рекурсивный алгоритм вычисления факториала с применением декоратора lru_cache.
    """

    if n == 0:
        return 1
    else:
        return n * recursion_factorial_lru(n - 1)


@lru_cache
def recursion_fib_lru(n):
    """
    Рекурсивный алгоритм вычисления числа Фибоначчи с применением декоратора lru_cache.
    """

    if 1 >= n >= 0:
        return n
    else:
        return recursion_fib_lru(n - 2) + recursion_fib_lru(n - 1)


if __name__ == '__main__':
    """
    Определение среднего времени работы алгоритмов нахождения факториалов 
    чисел и чисел Фибоначии рекурсивними алгоритмами и итеративными 
    алгоритмами, а также с применением декоратора lru_cache и без него.
    """

    # Найдем среднее время, которое требуется для вычисления факториала числа рекурсивным алгоритмом.
    for i in range(10, 30):
        str_i = str(i)
        time_work = timeit.timeit("recursion_factorial("+str_i+")", globals=globals(), number=20)
        print(f'Время выполнения рекурсивного алгоритма вычисления '
              f'факториала для', i, '-го числа =', time_work, 'сек.')
    print('\n')

    # Найдем среднее время, которое требуется для вычисления факториала числа итеративным алгоритмом.
    for i in range(10, 30):
        str_i = str(i)
        time_work = timeit.timeit("iterative_factorial("+str_i+")", globals=globals(), number=20)
        print(f'Время выполнения итеративного алгоритма вычисления '
              f'факториала для', i, '-го числа =', time_work, 'сек.')
    print('\n')

    # Найдем среднее время, которое требуется для вычисления факториала
    # числа рекурсивным алгоритмом с применением декоратора lru_cache.
    for i in range(10, 30):
        str_i = str(i)
        time_work = timeit.timeit("recursion_factorial_lru("+str_i+")", globals=globals(), number=20)
        print(f'Время выполнения рекурсивного алгоритма вычисления '
              f'факториала с lru_cache для', i, '-го числа =', time_work, 'сек.')
    print('\n')

    # Найдем среднее время, которое требуется для вычисления n-го числа Фибоначчи рекурсивным алгоритмом.
    for i in range(15, 25):
        str_i = str(i)
        time_work = timeit.timeit("recursion_fib(" + str_i + ")", globals=globals(), number=20)
        print(f'Время выполнения рекурсивного алгоритма вычисления',
              i, '-го числа Фибоначчи =', time_work, 'сек.')
    print('\n')

    # Найдем среднее время, которое требуется для вычисления n-го числа Фибоначчи итеративным алгоритмом.
    for i in range(15, 25):
        str_i = str(i)
        time_work = timeit.timeit("iterative_fib(" + str_i + ")", globals=globals(), number=20)
        print(f'Время выполнения итеративного алгоритма вычисления',
              i, '-го числа Фибоначчи =', time_work, 'сек.')
    print('\n')

    # Найдем среднее время, которое требуется для вычисления n-го числа
    # Фибоначчи рекурсивным алгоритмом с применением декоратора lru_cache.
    for i in range(15, 25):
        str_i = str(i)
        time_work = timeit.timeit("recursion_fib_lru(" + str_i + ")", globals=globals(), number=20)
        print(f'Время выполнения рекурсивного алгоритма вычисления',
              i, '-го числа Фибоначчи с применением декоратора lru_cache =', time_work, 'сек.')
    print('\n')
