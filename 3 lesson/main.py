from random import randint


class GAME1:
    def __init__(self):
        self.num1: int = int(1)
        self.num2: int = int(10)
        self.number: int = int(randint(self.num1, self.num2))

    def validate(self, guess: int):
        if self.guess < self.number:
            val: str = '\nТвое число меньше загаданного.'
            print(val)
            return False
        elif self.guess > self.number:
            val: str = '\nТвое число больше загаданного.'
            print(val)
            return False
        else:
            val: str = '\nУгадал!'
            print(val)
            return exit(0)

    def engine(self):
        if game_mode == 1:
            print('\nУгадай число между 1 и 10!')
            while True:
                self.guess: int = int(input('Введи число:'))
                self.validate(self.guess)
        else:
            while True:
                current_num: int = randint(self.num1, self.num2)
                print("Пытаюсь отгадать (от 1 до 10), твое число :", current_num, "?")
                enter: str = input("\n Угадал '=', больше '>' ,меньше '<':")
                if enter == '>':
                    self.num1 = current_num + 1
                    GAME2.checking(self.num1)
                elif enter == '<':
                    self.num2 = current_num - 1
                    GAME2.checking(self.num2)
                elif enter == '=':
                    print('Я угадал, твое число: ' + str(current_num))
                    return True


class GAME2(GAME1):
    @staticmethod
    def checking(num: int):
        if not 0 < num < 11:
            print('Обманываешь!')
            exit(0)
        else:
            return False


game_mode: int = int(input('Доступные игры: \n 1. Я загадываю число \n 2. Ты загадываешь число\n\n Ввод режима: '))
if game_mode == 1:
    run = GAME1()
    run.engine()
elif game_mode == 2:
    run = GAME2()
    run.engine()
else:
    print('Некорректный ввод! Аварийное завершение')
    exit(0)

