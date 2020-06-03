"""Main random number script code."""
import random

import prompt


def run():
    """Run main function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    def random_number():
        count = 0
        while count != 3:
            number = random.randint(1, 100)  # noqa: S311
            print(f'Question: {number}')
            answer = prompt.string('Your answer: ')

            if number % 2 == 0 and answer == 'yes':
                print('Correct!')
                count += 1
            elif number % 2 != 0 and answer == 'no':
                print('Correct!')
                count += 1
            elif number % 2 == 0 and answer == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {0}!".format(name))
                break
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {0}!".format(name))
                break
        else:
            print('Congratulations, {0}!'.format(name))

    random_number()
