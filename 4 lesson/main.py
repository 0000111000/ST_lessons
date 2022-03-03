from random import randint


class GAMES:
    def __init__(self):
        self.num1: int = int(1)
        self.num2: int = int(10)
        self.number: int = int(randint(self.num1, self.num2))


    def startup(self):
        game_mode: int = int(
            input('Доступные игры: \n 1. Я загадываю число \n 2. Ты загадываешь число\n\n Ввод режима: '))
        if game_mode == 1:
            run = GAME1()
            run.engine()
        elif game_mode == 2:
            run = GAME2()
            run.game_main(self.num1, self.num2)
        else:
            print('Некорректный ввод! Аварийное завершение')
            exit(0)

    @staticmethod
    def usr_guess_validate(num: int):
        assert 0 < num < 11, "Обанываешь!"
        return False
        # if not 0 < num < 11:
        #     print('Обманываешь!')
        #     exit(0)
        # else:
        #     return False


class GAME1 (GAMES):

    def engine(self):
            print('\nУгадай число между 1 и 10!')
            self.game_main()


    def game_main(self):
        while True:
            try:
                guess: int = int(input('Введи число:'))
                if guess < self.number:
                    print('\nТвое число меньше загаданного.')
                elif guess > self.number:
                    print('\nТвое число больше загаданного.')
                else:
                    print('\nУгадал!')
                    return exit(0)
            except ValueError as ve:
                print('Ты ввел неверное значение')


class GAME2(GAMES):

    def game_main(self, num1, num2):
        while True:
            current_num: int = randint(num1, num2)
            print("Пытаюсь отгадать (от 1 до 10), твое число :", current_num, "?")
            enter: str = input("\n Угадал '=', больше '>' ,меньше '<':")
            if enter == '>':
                num1 = current_num + 1
                GAMES.usr_guess_validate(num1)
            elif enter == '<':
                num2 = current_num - 1
                GAMES.usr_guess_validate(num2)
            elif enter == '=':
                print('Я угадал, твое число: ' + str(current_num))
                return True


startup = GAMES()
startup.startup()


