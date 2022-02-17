import random


class Game:
    def __init__(self):
        self.number = int(random.randint(1, 10))

    def validate(self, guess: int):
        while True:
            if self.guess < self.number:
                val = '\nТвое число меньше загаданного.'
                print(val)
                self.mainGame()
                break
            elif self.guess > self.number:
                val = '\nТвое число больше загаданного.'
                print(val)
                self.mainGame()
                break
            else:
                val = '\nУгадал!'
                print(val)
                break

    def mainGame(self):
        self.guess = int(input('\nУгадай число между 1 и 10: \n'))
        self.validate(self.guess)


c = Game()
c.mainGame()
