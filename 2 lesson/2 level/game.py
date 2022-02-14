import random
number = int(random.randint(1, 10))
class SEEKER:
    @staticmethod
    def seek():
        answ = int(0)
        while answ != number:
            guess = int(input('Угадай число между 1 и 10: \n'))
            answ = guess
            if guess < number:
                print('\nТвое число меньше загаданного.')
                continue
            if guess > number:
                print('\nТвое число больше загаданного.')
                continue
            if guess == number:
                print('\nУгадал!')
                break


c = SEEKER()
c.seek()
