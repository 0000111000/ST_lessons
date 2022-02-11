import random

number = int(random.randint(1, 10))
guess = 0

while guess != number:
    guess = int(input('Угадай число между 1 и 10: \n'))

    if guess < number:
            print('\nТвое число меньше загаданного.')

    if guess > number:
            print('\nТвое число больше загаданного.')

    if guess == number:
            print('\nУгадал!')
            break

