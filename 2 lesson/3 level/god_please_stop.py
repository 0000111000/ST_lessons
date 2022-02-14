import random
calc = int(random.randint(1, 10))
out = str()


class GAME:
    def __init__(self):
        val = str(out)
        number = int(calc)

    @classmethod
    def output(cls, val: str):
        print(val)

    @classmethod
    def validate(cls, number: int):
        guess = int
        while guess != number:
            guess = int(input('\nУгадай число между 1 и 10: \n'))
            if guess < number:
                val = '\nТвое число меньше загаданного.'
                cls.output(val)
            if guess > number:
                val = '\nТвое число больше загаданного.'
                cls.output(val)
            if guess == number:
                val = '\nУгадал!'
                cls.output(val)


c = GAME()
c.validate(calc)
c.output(out)
