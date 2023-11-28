#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_number_sum_representations(n, i=1, output=""):
    """
    Печатает все возможные представления числа n в виде суммы других натуральных чисел.

    Аргументы:
    - n (int): Натуральное число, для которого ищутся представления в виде суммы.
    - i (int): Текущее число для добавления к сумме.
    - output (str): Строка, представляющая текущее представление суммы.
    """
    if n == 0:
        print(output)
        return
    if n < 0:
        return
    while i <= n:
        print_number_sum_representations(n - i, i, f"{output} + {i}" if output else str(i))
        i += 1


if __name__ == '__main__':
    n = int(input("Введите число, которое хотите представить в виде сумм: "))
    print_number_sum_representations(n)
