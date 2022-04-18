#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально
задействовав имеющиеся в Python средства перегрузки операторов.

Поле first — целое число, левая граница диапазона, включается в
диапазон; поле second — целое число, правая граница диапазона,
не включается в диапазон. Пара чисел представляет полуоткрытый
интервал [first, second). Реализовать метод —
проверку заданного целого числа на принадлежность диапазону
"""


class InRange:

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def __contains__(self, other):
        if isinstance(other, InRange):
            return self.first <= other.first < self.second
        else:
            return False


if __name__ == "__main__":
    interval = InRange(first=2, second=10)
    x = InRange(first=6)
    print(f"Число находится в диапазоне: {x in interval}")
    print(f"Число вне диапазона: {x not in interval}")

