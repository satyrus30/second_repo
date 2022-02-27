import random

'''
1 Создаем игровое поле
- генерируем поле
- делаем разметку координат
- заполняем поле '-'

2 Игрок 1 - 'Х'
Игрок 2 - 'O'

3 Делаем ход
- отправляем координаты хода на доску
- проверяем что там знак '-' поле устанавливаем в зависимости от игрока
либо 'Х' либо 'O'
- после смены знака ход переходит к следующему игроку

Ходы делаем до тех пор пока:
- не кончатся знаки '-'
- либо один из игроков не пободит

4 Победа :
- горизонталь или вертикаль или диагональ не будет состоять,
 только из знаков  либо 'Х' либо 'O'

Конец игры
'''

def DefaultField(size):
    bareField = []
    for i in range(size):
        bareField.append([])
        for j in range(size):
            bareField[i].append('-')
    return bareField

def PrintField(field, size):
    print('  ', end='')
    for i in range(size):
        print(i, end=' ')
        
    print()
    for i in range(size):
        print(i, end=' ')
        for j in range(size):
            print(field[i][j], end=' ')
        print()

def CheckingPlacement(field, size, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= 0 and x + i <= size:
                if y + j >= 0 and y + j <= size:
                    if field[x][y] != '-':
                        return False
    return True

def Installing(field, mark, x, y):
    if mark == 0:
        field[x][y] = 'X'
    elif mark == 1:
        field[x][y] = 'O'
    return field

def CheckWinner(field, size, mark):
    if mark == 0:
        # мой первый вариант
        # for i in range(x, size):
        #     if field[i][y] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         return
        # for i in range(x, -1, - 1):
        #     if field[i][y] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         return
        # for i in range(y, size):
        #     if field[x][i] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         return
        # for i in range(y, -1, - 1):
        #     if field[x][i] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         return
        for i in range(size):  # горизонт / вертикаль
            count = 0
            for j in range(size):
                if field[i][j] != 'X':
                    break
                else:
                    count += 1
                    if count == 3:
                        return True

        for i in range(size):
            count = 0
            for j in range(size):
                if field[j][i] != 'X':
                    break
                else:
                    count += 1
                    if count == 3:
                        return True

    elif mark == 1:
        # for i in range(x, size):
        #     if field[i][y] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         break
        # for i in range(x, -1, - 1):
        #     if field[i][y] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         break
        # for i in range(y, size):
        #     if field[x][i] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         break
        # for i in range(y, -1, - 1):
        #     if field[x][i] == 'X':
        #         count += 1
        #         if count == 3:
        #             return True
        #         continue
        #     else:
        #         break
        for i in range(size):  # горизонт
            count = 0
            for j in range(size):
                if field[i][j] != 'O':
                    break
                else:
                    count += 1
                    if count == 3:
                        return True

        for i in range(size):
            count = 0
            for j in range(size):
                if field[j][i] != 'O':
                    break
                else:
                    count += 1
                    if count == 3:
                        return True


def CheckingDiagonal(field, size, mark):
    if mark == 0:
        count = 0
        for i in range(size):
            if field[i][i] == 'X':
                count += 1
                if count == 3:
                    return True

        count = 0
        for i in range(size - 1, -1, -1):
            if field[i][size - i - 1] == 'X':
                count += 1
                if count == 3:
                    return True

    elif mark == 1:
        count = 0
        for i in range(size):
            if field[i][i] == 'O':
                count += 1
                if count == 3:
                    return True

        count = 0
        for i in range(size - 1, -1, -1):
            if field[i][size - i - 1] == 'O':
                count += 1
                if count == 3:
                    return True

    return False

def main():
    # 1 Создаем игровое поле
    size = int(input('Размер поля?'))
    # крестик
    markCross = 0
    # нолик
    markZero = 1
    playingField = DefaultField(size)
    PrintField(playingField, size)

    # 3 Делаем ход
    player = 0
    while True:
        if player == 0:
            print('Игрок 1')
            print('Введите координаты')
            x = int(input('X --->'))
            y = int(input('Y --->'))
            if CheckingPlacement(playingField, size, x, y) == True:
                Installing(playingField, markCross, x, y)
                PrintField(playingField, size)
            else:
                while True:
                    print('Некорректные координаты, попробуйте ещё')
                    PrintField(playingField, size)
                    print('Игрок 1')
                    print('Введите координаты')
                    x = int(input('X --->'))
                    y = int(input('Y --->'))
                    if CheckingPlacement(playingField, size, x, y) == True:
                        Installing(playingField, markCross, x, y)
                        PrintField(playingField, size)
                        break
            if CheckWinner(playingField, size, markCross) == True or\
                    CheckingDiagonal(playingField, size, markCross) == True:
                print('Победа')
                break

        else:
            print('Игрок 2')
            print('Введите координаты')
            x = int(input('X --->'))
            y = int(input('Y --->'))
            if CheckingPlacement(playingField, size, x, y) == True:
                Installing(playingField, markZero, x, y)
                PrintField(playingField, size)
            else:
                while True:
                    print('Некорректные координаты, попробуйте ещё')
                    PrintField(playingField, size)
                    print('Игрок 1')
                    print('Введите координаты')
                    x = int(input('X --->'))
                    y = int(input('Y --->'))
                    if CheckingPlacement(playingField, size, x, y) == True:
                        Installing(playingField, markZero, x, y)
                        PrintField(playingField, size)
                        break
            if CheckWinner(playingField, size, markZero) == True or \
                    CheckingDiagonal(playingField, size, markZero) == True:
                print('Победа')
                break

        player = (player + 1) % 2


if __name__ == '__main__':
    main()
