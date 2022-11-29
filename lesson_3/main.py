# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции. Пример: [2, 3, 5, 9, 3] ->
# на нечётных позициях элементы 3 и 9, ответ: 12
list = [2, 3, 5, 9, 3]
sum = 0
for i in range(0, len(list)):
    sum += list[i] if i % 2 != 0 else 0
print('Ответ для задачи 1: ' + f'{sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
list = [2, 3, 4, 5, 6]
length = len(list)
mult = []
for i in range(0, int(length / 2)):
    mult.append(list[i] * list[length - 1 - i])
if length % 2 != 0:
    mult.append(list[int(length / 2)] ** 2)
print('Ответ для задачи 2: ' + f'{mult}')

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list = [1.1, 1.2, 3.1, 5.01, 10.01]
max_fraction = list[0] - int(list[0])
min_fraction = max_fraction
for i in range(1, len(list)):
    fraction = list[i] - int(list[i])
    if fraction > max_fraction:
        max_fraction = fraction
    if fraction < min_fraction:
        min_fraction = fraction
print('Ответ для задачи 3: ' + f'{round((max_fraction - min_fraction), 4)}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101, 3 -> 11, 2 -> 10
# number = int(input('Введите число: '))
number = 10
string = ''
while number > 0:
    string += str(number % 2)
    number = int(number / 2)
print('Ответ для задачи 4: ' + string[::-1])

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# number = int(input('Введите число: '))
number = 10
fibonacci_plus = [0, 1]
fibonacci_minus = []
for i in range(1, number):
    fibonacci_plus.append(fibonacci_plus[i] + fibonacci_plus[i - 1])
for i in range(number, 1, -1):
    fibonacci_minus.append(int(fibonacci_plus[i] * (-1) ** (-i + 1)))
print('Ответ для задачи 5: ' + f'{fibonacci_minus + fibonacci_plus}')
