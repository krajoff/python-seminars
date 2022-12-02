import math
from random import randint
import string

# 1. Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# number = float(input('Введите число: '))
# dec = input('Введите необходимую точность для числа: ')
# if float(dec) >= 10**(-1) and float(dec) <= 10**(-10):
#     print('Неверная точность')
# else:
#     print(f'{round(number, len(dec)-2)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# number = int(input('Введите натуральное число: '))
# list = [1]
# if number >= 2 and number % 2 == 0:
#     list.append(2)
# for i in range(3, int(number/2), 2):
#     if number % i == 0:
#         list.append(i)
#         while number % i == 0:
#             number /= i
# print(list)

# 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.
# int_list = [randint(1, 10) for _ in range(10)]
# no_repeat_list = list(set(int_list))
# print('Исходный список: ' + f'{int_list}')
# print('Список без повторений: ' + f'{no_repeat_list}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"}
trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))
k = int(input('Введите степень: '))
int_list = [randint(0, 100) for _ in range(k + 1)]
count = 0
for i in int_list:
    if i != 0:
        if count != k and count != k - 1:
            print(f'{i}*x' + f'{k - count}'.translate(trans), end=' + ')
        elif count != k:
            print(f'{i}*x', end=' + ')
        else:
            print(f'{i}', end='')
    count += 1
print(' = 0', end='')

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
