import random

# 1. Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр. Пример: 6782 -> 23, 0,56 -> 11
string = input('Введите число: ')
summarize = 0
for i in string:
    if i != ',' and i != '.':
        summarize += int(i)
print(summarize)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number = int(input('Введите число: '))
factorials = [1]
for i in range(1, number):
     factorials.append(factorials[i-1]*(i+1))
print(factorials)

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input('Введите число: '))
serials = [round((1 + 1/n)**n, 2) for n in range(1, n + 1)]
print(serials)

# 4.Реализуйте алгоритм перемешивания списка.
n = int(input('Введите число: '))
list = [n for n in range(1, n + 1)]
print('Всё по порядку: ', list)
random.shuffle(list)
print('Всё вразнобой: ', list)
