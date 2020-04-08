'''While "Functional programming" isn't easy for me, but it's while)

Tasks from Hexlet:

keep_truthful Эта функция должна принимать на вход итерируемый источник значений и возвращать итератор, 
отдающий только те значения из источника, которые "истинны" (вам пригодится функция operator.truth).

abs_sum Функция abs_sum принимает на вход итерируемый источник чисел. Вернуть же функция должна сумму абсолютных 
значений этих чисел (используйте sum и abs).

walk walk должна для некоего словаря с глубокой вложенностью уметь доставать значение по указанному в виде 
iterable строк пути. В решении можете использовать функцию operator.getitem.'''

import operator
from operator import getitem
from functools import reduce


def keep_truthful(a):
    return filter(operator.truth, a)


def abs_sum(a):
    b = list(map(abs, a))
    x = 0
    for i in b:
        x += i
    return x


def walk(dic, keys):
    return reduce(getitem, keys, dic)
