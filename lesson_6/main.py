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
                if idx == len(instr) - 2:
                    res += instr[idx] if cnt == 1 else instr[idx] + str(cnt)
                    cnt = 1
            else:
                res += instr[idx] if cnt == 1 else instr[idx] + str(cnt)
                cnt = 1
                if idx == len(instr) - 2:
                    res += instr[idx + 1] if cnt == 1 else instr[idx + 1] + str(cnt)
            idx += 1
        return res


print('Задача 2:\nВходная строка: ' f'{string}')
print('Результат: ' + compress(string) + '\n')
