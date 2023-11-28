#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


# Декоратор для оптимизации хвостовой рекурсии
class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        """
        Инициализирует экземпляр TailRecurseException.

        Аргументы:
        - args (tuple): Аргументы для функции.
        - kwargs (dict): Именованные аргументы для функции.
        """
        self.args = args
        self.kwargs = kwargs


def tail_recursive(func):
    def wrapper(*args, **kwargs):
        """
        Обёртка для функции для имитации хвостовой рекурсии.

        Аргументы:
        - args: Аргументы для функции.
        - kwargs: Именованные аргументы для функции.
        """
        while True:
            try:
                return func(*args, **kwargs)
            except TailRecurseException as e:
                args = e.args
                kwargs = e.kwargs
                continue

    return wrapper


@tail_recursive
def factorial(n, accumulator=1):
    """
    Рекурсивная функция для вычисления факториала.

    Аргументы:
    - n (int): Число для вычисления факториала.
    - accumulator (int): Аккумулятор для промежуточных результатов.

    Возвращает:
    - int: Факториал числа n.
    """
    if n == 0:
        return accumulator
    else:
        raise TailRecurseException((n - 1, n * accumulator), {})


@tail_recursive
def fib(n, a=0, b=1):
    """
    Рекурсивная функция для вычисления чисел Фибоначчи.

    Аргументы:
    - n (int): Число в последовательности Фибоначчи.
    - a (int): Первое число в последовательности.
    - b (int): Второе число в последовательности.

    Возвращает:
    - int: n-ное число в последовательности Фибоначчи.
    """
    if n == 0:
        return a
    else:
        raise TailRecurseException((n - 1, b, a + b), {})


if __name__ == '__main__':
    # Оценка времени выполнения функций
    print("Время выполнения рекурсивной функции factorial:", timeit.timeit(lambda: factorial(20), number=10000))
    print("Время выполнения рекурсивной функции fib:", timeit.timeit(lambda: fib(20), number=10000))
