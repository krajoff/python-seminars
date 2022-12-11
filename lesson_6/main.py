import math
import pandas as pd

# 5. Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это
# множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры: [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11",  [1,4,3,2] => "1-4", [1,4] => "1,4"
# some_list = [1, 4, 5, 2, 3, 9, 8, 11, 0]
import sys

some_list = [1, 4, 3, 2]
# some_list = [1, 4]
some_list.sort()
string = ''
cnt = 0
for i in range(0, len(some_list) - 1):
    if some_list[i] == some_list[i + 1] - 1:
        if cnt == 0:
            first = some_list[i]
        cnt += 1
        string += f'{first}-{some_list[i + 1]}' \
            if i + 1 == len(some_list) - 1 else ''
    else:
        string += f'{first}-{some_list[i]},' if cnt > 0 \
            else f'{some_list[i]},{some_list[i + 1]}'
        string += f'{some_list[i + 1]}' \
            if i + 1 == len(some_list) - 1 and len(some_list) != 2 else ''
        cnt = 0
print('Задача 1:\nВходная строка: ' f'{some_list}')
print('Результат: ' + string + '\n')

# 6. Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку , если на вход пришла невалидная строка. Пояснения:
# Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза,
# к нему добавляется количество повторений
string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'


def compress(instr: str):
    if instr == '':
        return 'Ошибка. Пустая строка'
    elif any(i.isdigit() for i in string):
        return 'Ошибка. Содержится цифра'
    else:
        idx = 0
        res = ''
        cnt = 1
        while idx < len(instr) - 1:
            if instr[idx] == instr[idx + 1]:
                cnt += 1
            else:
                res += instr[idx] if cnt == 1 else instr[idx] + str(cnt)
                cnt = 1
            idx += 1
        else:
            res += str(cnt) + instr[idx]
        return res


print('Задача 2:\nВходная строка: ' f'{string}')
print('Результат: ' + compress(string) + '\n')


# 7. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовём самой далёкой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далёкая планета. Круговые
# орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники
# были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далёкой планеты. Каждая орбита представляет из себя кортеж из пары чисел –
# полуосей её эллипса. Площадь эллипса вычисляется по формуле S = πab, где a и b – длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далёкая планета ровно одна. Ввод orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Вывод 2.5 10


def find_farthest_orbit(list_of_orbits):
    filtered_list = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    list_square = [math.pi * orbit[0] * orbit[1] for orbit in filtered_list]
    max_orbit = list_square.index(max(list_square))
    return filtered_list[max_orbit]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print('Задача 3:\nВходная строка: ' f'{orbits}')
print('Результат: ' + f'{find_farthest_orbit(orbits)}' + '\n')


def print_operation_table(operation, num_rows, num_columns):
    table = []
    for k in range(1, num_rows):
        row = list(map(operation, [x for x in range(1, num_columns)], [k for _ in range(1, num_columns)]))
        table.append(row)
    print(pd.DataFrame(table, columns=[i for i in range(1, num_columns)], index=[i for i in range(1, num_rows)]))


print('Задача 4')
print_operation_table(lambda x, y: x * y, 10, 10)
