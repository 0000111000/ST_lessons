import random


class Game:
    def __init__(self):
        self.number = int(random.randint(1, 10))

    def validate(self, guess: int):
        if self.guess < self.number:
            val = '\nТвое число меньше загаданного.'
            print(val)
            return False
        elif self.guess > self.number:
            val = '\nТвое число больше загаданного.'
            print(val)
            return False
        else:
            val = '\nУгадал!'
            print(val)
            return exit(0)

    def mainGame(self):
        print('Угадай число между 1 и 10\n')
        while True:
            self.guess = int(input('\nВведи число: \n'))
            self.validate(self.guess)


c = Game()
c.mainGame()
