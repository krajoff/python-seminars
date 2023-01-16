# Напишите класс TicTacToeBand для игры в крестики-нолики, который должен иметь следующие методы:
# new_game() - создание новой игры, get_field() - для получения поля (список списков),
# check_field() - проверка если победитель, который возвращает Х, если победил первый игрок 0, если второй D,
# если ничья и None, если можно продолжить игру. make_move(row, col) - который устанавливает значение текущего
# хода в ячейку поля с координатами row и col, если это возможно, "переключает ход игрока, а также возращает сообщение
# "Победил игрок Х" при победе крестиков и "Продолжаем играть",  если победитель после данного хода неопределен.

class TicTacToeBand:
    end_game = False

    def __init__(self):
        self.ttt = None
        self.cnt = 1
        self.anq = True

    def new_game(self):
        self.ttt = [['_', '_', '_'] for _ in range(0, 3)]

    def get_field(self):
        if self.ttt is None:
            self.new_game()
            for j in range(0, 3):
                print(self.ttt[j])
        else:
            for j in range(0, 3):
                print(self.ttt[j])

    def check_field(self):
        for i in range(0, 3):
            if self.ttt[0][i] == self.ttt[1][i] == self.ttt[2][i] == 'X' or \
                    self.ttt[i][0] == self.ttt[i][1] == self.ttt[i][2] == 'X':
                print('Х - победитель')
            elif self.ttt[0][i] == self.ttt[1][i] == self.ttt[2][i] == '0' or \
                    self.ttt[i][0] == self.ttt[i][1] == self.ttt[i][2] == '0':
                print('0 - победитель')
        if self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] == 'X' or \
                self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] == 'X':
            print('X - победитель')
        elif self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2] == '0' or \
                self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0] == '0':
            print('0 - победитель')
        elif any('_' in el for el in self.ttt):
            print('Можно продолжить игру')
        else:
            print('D - ничья')

    def make_move(self, row, col):
        if self.ttt[row][col] == '_':
            if self.cnt == 0:
                self.ttt[row][col] = '0'
                self.cnt = 1
            else:
                self.ttt[row][col] = 'X'
                self.cnt = 0
            self.check_field()
        else:
            print('Данное место уже занято!')


board = TicTacToeBand()
board.get_field()
board.make_move(1, 1)
board.make_move(0, 1)
board.make_move(0, 0)
board.make_move(0, 2)
board.make_move(2, 2)
board.get_field()
