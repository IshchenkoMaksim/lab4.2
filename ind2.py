#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать метод
size(), возвращающий установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения size и count
устанавливаются конструктором.

Реализовать класс Money, используя для представления суммы денег список словарей.
Словарь имеет два ключа: номинал купюры и количество купюр данного достоинства.
Номиналы представить как строку. Элемент списка словарей с меньшим индексом
содержит меньший номинал."""

from copy import deepcopy


def sort(ls):
    return sorted(ls, key=lambda k: k['denomination'])


class Money:

    def __init__(self, money):
        count = 8
        self.money = money
        if len(self.money) > count:
            print("Превышен размер списка")

    def size(self):
        return len(self.money)

    def sort_ob(self):
        self.money = sorted(self.money, key=lambda k: k['denomination'])
        return "Список отсортирован"

    def __getitem__(self, key):
        return self.money[key]

    def __add__(self, other):
        d = deepcopy(self.money)
        for i in range(len(self.money)):
            d[i]['count'] = self.money[i]['count'] + other[i]['count']
        self.money = d

        return self.money

    def __sub__(self, other):
        d = deepcopy(self.money)
        for i in range(len(self.money)):
            d[i]['count'] = self.money[i]['count'] - other[i]['count']
        self.money = d

        return self.money


if __name__ == '__main__':
    l1 = Money([{"denomination": 100, "count": 56}, {"denomination": 500, "count": 56},
                {"denomination": 200, "count": 156}, {"denomination": 1000, "count": 34}])
    l2 = [{"denomination": 500, "count": 333}, {"denomination": 100, "count": 1000},
          {"denomination": 1000, "count": 600}, {"denomination": 200, "count": 50}]
    l3 = [{"denomination": 200, "count": 55}, {"denomination": 100, "count": 100},
          {"denomination": 500, "count": 60}, {"denomination": 1000, "count": 20}]
    print(l1.sort_ob())
    l2 = sort(l2)
    print(l1.size())
    print(f"l1 + l2 = {l1 + l2}")
    print(f"l1 - l3 = {l1 - l3}")
    print(l1[3])
