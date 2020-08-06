"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

#  Решение задачи №1.

from random import randint
import time

# Измерение времени выполнения скрипта.
start_time = time.time()
array = []
print("--- %s seconds ---" % (time.time() - start_time))

# Количество элементов списка.

N = 10
array = []

for i in range(N):
    array.append(randint(1, 99))

for i in array:
    print(i, end='')
print()

import time

# Измерение времени выполнения скрипта.
start_time = time.time()
d = []
print("--- %s seconds ---" % (time.time() - start_time))

# Количество элементов словаря.
d = {a: 1 + a for a in range(100)}
print(d)

import random
import time

# Измерение времени выполнения скрипта.
start_time = time.time()
rand = []
print("--- %s seconds ---" % (time.time() - start_time))

# Кортеж получение случайных значиней.
rand = random.uniform(0, 1)
print(rand)