#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def min_recursive(list_x, n, border_n, min_element):
    """
    Рекурсивная функция поиска минимума среди элементов от n-го элемента до конца списка X.
    """
    if list_x[border_n] < min_element:
        min_element = list_x[border_n]
    if border_n == n - 1:
        return min_element
    else:
        return min_recursive(list_x, n, border_n + 1, min_element)


if __name__ == '__main__':
    """
    Дан список X из целых n вещественных чисел. Необходимо найти минимальный 
    элемент списка, используя вспомогательную рекурсивную функцию, находящую 
    минимум среди последних элементов списка X, начиная с n-го.
    """

    n = int(input("Введите количество элементов в списке X: "))
    # Создадим список X указанной длины из случайных элементов.
    list_x = [random.randint(-1000, 1000) for i in range(n + 1)]
    border_n = int(input("Введите номер элемента с которого необходимо искать минимальный элемент списка X: "))
    min_element = list_x[border_n]

    print("Минимальный элемент начиная с", border_n, "-го в списке вещественных чисел = ",
          min_recursive(list_x, n, border_n, min_element))
