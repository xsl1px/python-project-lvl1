"""Main random number script code."""
import random
import prompt
import math


def run():
    """Run main function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    def expression():
        count = 0
        while count != 3:
            num1 = random.randint(1, 100)  # noqa: S311
            num2 = random.randint(1, 100)  # noqa: S311
            print(f'Question: {num1} {num2}')
            gcd = math.gcd(num1, num2)
            answer = prompt.string('Your answer: ')

            if answer == gcd:
                print('Correct!')
                count += 1
            else:
                print(f'{answer} is wrong answer ;(. Correct answer was {gcd}!')
                break
        else:
            print('Congratulations, {0}!'.format(name))

    expression()
