from gameparts import Board
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки.
    row = int(input('Введите номер строки: '))

    column = int(input('Введите номер столбца: '))
    if column < 0 or column >= game.field_size:
        raise FieldIndexError

    column = int(input('Введите номер столбца: '))
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()