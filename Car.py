'''
1. Создавать доску
2. Печать доску

'''


class Player:
    def __init__(self):
        self.countWin = 0


class Board:
    def __init__(self, size):
        self.size = size # private
        self.field = []

    def createBoard(self):
        self.field.clear()
        for i in range(self.size):
            self.field.append('_')

    def changeCell(self, pos, elem):
        self.field[pos] = elem

    def printBoard(self):
        print('S', (((self.size-2) * 2) + 1) * ' ', 'F', sep='')
        for i in range(self.size):
            print(self.field[i], end=' ')


class Car:
    def __init__(self, sign):
        self.pos = 0
        self.sign = sign


class Game:
    def __init__(self):
        self.__board = None
        self.__players = []
        self.__activePlayer = None
        self.__winNumber = 1 # 3
        self.__car = None
        self.__finishGame = None

    def createNewGame(self, size):
        self.__finishGame = False

        self.__car = Car('Д')

        self.__board = Board(size)
        self.__board.createBoard()
        self.__board.changeCell(self.__car.pos, self.__car.sign)

        self.__activePlayer = 0

        self.__players.clear()
        for i in range(2):
            self.__players.append(Player())


    def __checkX(self, x):
        if x > 2 or x < -2 or x == 0:
            return False

        if x + self.__car.pos >= self.__board.size \
                or x + self.__car.pos < 0:
            return False

        return True


    def __checkWin(self, num):
        if self.__players[num].countWin == self.__winNumber:
            return True

        if self.__car.pos == self.__board.size - 1:
            return True


        return False

    def printGame(self):
        print('Player', self.__activePlayer)
        self.__board.printBoard()

    def printBoard(self):
        self.__board.printBoard()

    def hod(self, x):
        if self.__checkX(x) == True:
            self.__board.changeCell(self.__car.pos, '_')
            self.__car.pos += x
            self.__board.changeCell(self.__car.pos, self.__car.sign)

            if self.__checkWin(self.__activePlayer) == True:
                self.__finishGame = True
            else:
                self.__activePlayer = (self.__activePlayer + 1) % len(self.__players)

    def isContinue(self):
        if self.__finishGame == False:
            return True
        return False

    def whoWin(self):
        return self.__activePlayer


    def play(self):
        while self.isContinue():
            self.printGame()
            print()
            print('X: ')
            x = int(input())
            self.hod(x)

        print('Player', self.whoWin(), 'win!')




def main():
    game = Game()
    game.createNewGame(int(input()))
    game.play()




if __name__ == '__main__':
    main()




'''
1) 
- игра до 3 побед игрока
- разные размеры для карты от 4 до 10

createNewRound - создать новый раунд (в игре может быть от 3 до 5 раундов, до 3 побед)
checkWinRount - кто победил в раунде
playRound - играть один раунд
___________________


2) ХО - доработать

3) json файлы

4) МБ - выделить классы (объекты)

'''





# b = Board(10)
# b.createBoard()
# b.createBoard()
# b.printBoard()







# '12.02.2020'
# date.d = 12
# date.m = 2
# date.y = 2020
    #set()
    #get()