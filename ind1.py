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

    def __lt__(self, other):
        return other < self.first

    def __gt__(self, other):
        return other > self.second

    def __eq__(self, other):
        return self.first <= other < self.second

    def __contains__(self, other):
        return self.first <= other < self.second


if __name__ == "__main__":
    interval = InRange(first=2, second=10)
    x = 4
    print(f"Число вне диапазона и больше него: {interval > x}")
    print(f"Число вне диапазона и меньше него: {interval < x}")
    print(f"Число в диапазоне: {interval == x}")
    print(f"Число находится в диапазоне: {x in interval}")
    print(f"Число вне диапазона: {x not in interval}")
