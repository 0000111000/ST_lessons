from random import randint


class GAME2:
    def __init__(self):
        self.num1 = int(1)
        self.num2 = int(10)


    @staticmethod
    def validate(num):
        if not 0 < num < 11:
            print('Обманываешь!')
            exit(0)
        else:
            return False


    def maingame(self):
        while True:
            current_num = randint(self.num1, self.num2)
            print(current_num)
            enter = input("Загадайте число от 1 до 10\n Угадал '=', больше '>' ,меньше '<':")
            if enter == '>':
                self.num1 = current_num + 1
                self.validate(self.num1)
            elif enter == '<':
                self.num2 = current_num - 1
                self.validate(self.num2)
            elif enter == '=':
                print('Я угадал, твое число: ' + str(current_num))
                return True


run = GAME2()
run.maingame()


