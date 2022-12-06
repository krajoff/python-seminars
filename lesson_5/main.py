import re
# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'Однажды, в студёную зимнюю пору \nЯ абв из лесу вышел; быабвл был сильный мороз'
for word in text.split():
    if 'абв' in word:
        text = text.replace(word + ' ', '')
print(text + '\n')


# 40. Создайте программу для игры в ""Крестики-нолики"".
# def check_end_game(fld: list) -> bool:
#     for i in range(0, 3):
#         if fld[0][i] == fld[1][i] == fld[2][i] in ['0', 'X'] or \
#                 fld[i][0] == fld[i][1] == fld[i][2] in ['0', 'X']:
#             print('Победа!')
#             return True
#     if fld[0][0] == fld[1][1] == fld[2][2] in ['0', 'X'] or \
#             fld[0][2] == fld[1][1] == fld[2][0] in ['0', 'X']:
#         print('Победа!')
#         return True
#     else:
#         return False
#
# print('Поле крестиков-ноликов - это поле 3х3: _ - это пустота, 0 - ноли, Х - крестик')
# tic_tac_toe = [['_', '_', '_'] for _ in range(0, 3)]
# OX = {0: '0', 1: 'X'}
# end_game = False
# cnt = 0
# anq = True
# while not end_game:
#     while anq:
#         cdt = list(map(int, input(f'Введите координаты {OX[cnt]} через пробел: ').split()))
#         if tic_tac_toe[cdt[0]][cdt[1]] == '_':
#             tic_tac_toe[cdt[0]][cdt[1]] = OX[cnt]
#             break
#         else:
#             print('Данное место уже занято!')
#     for i in range(0, 3):
#         print(tic_tac_toe[i])
#     end_game = check_end_game(tic_tac_toe)
#     cnt = 1 if cnt == 0 else 0


# 41. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
output = ''
cnt = 1
with open('input.txt', 'r', encoding='utf-8') as infile, \
        open('output.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        string = list(map(str, line.split()))
        for word in string:
            for i in range(0, len(word)-1):
                if word[i] == word[i+1]:
                    cnt += 1
                    if i == len(word)-2:
                        outfile.write(f'{cnt}{word[i]}')
                        cnt = 1
                else:
                    outfile.write(f'{cnt}{word[i]}')
                    cnt = 1
                    if i == len(word)-2:
                        outfile.write(f'{cnt}{word[i+1]}')
            outfile.write(' ')
        outfile.write('\n')

test_string = "There are 22apples for 4 persons"
res = [int(i) for i in test_string.split(r'\w+') if i.isdigit()]
print(res)

# with open('output.txt', 'r', encoding='utf-8') as infile, \
#         open('decode.txt', 'w', encoding='utf-8') as outfile:
#     for line in infile:
#         if
#             string = list(map(str, line.split()))
#         for word in string:
