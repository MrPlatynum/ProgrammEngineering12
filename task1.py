#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


# Итеративная версия чисел Фибоначчи
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Рекурсивная версия чисел Фибоначчи
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 2) + fib_recursive(n - 1)


# Итеративная версия факториала
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Рекурсивная версия факториала
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Измерение времени выполнения для итеративных функций
print("Итеративный факториал:", timeit.timeit('factorial_iterative(10)', globals=globals()))
print("Итеративные числа Фибоначчи:", timeit.timeit('fib_iterative(10)', globals=globals()))

# Измерение времени выполнения для рекурсивных функций
print("Рекурсивный факториал:", timeit.timeit('factorial_recursive(10)', globals=globals()))
print("Рекурсивные числа Фибоначчи:", timeit.timeit('fib_recursive(10)', globals=globals()))


# Декорируем рекурсивные функции для использования кэша
@lru_cache(maxsize=None)
def fib_recursive_cached(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive_cached(n - 2) + fib_recursive_cached(n - 1)


@lru_cache(maxsize=None)
def factorial_recursive_cached(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive_cached(n - 1)


# Измерение времени выполнения для кэшированных рекурсивных функций
print("Кэшированный рекурсивный факториал:", timeit.timeit('factorial_recursive_cached(10)', globals=globals()))
print("Кэшированные рекурсивные числа Фибоначчи:", timeit.timeit('fib_recursive_cached(10)', globals=globals()))
