"""Main Game Even code."""
import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_result():
    """Function returns result for engine.py from find_even_number function."""
    return find_even_number()


def find_even_number():
    """Function chooses random number from 1 to 100 and checks it for evenness."""
    min_number = 1
    max_number = 100
    number = random.randint(min_number, max_number)  # noqa: S311
    question = f'{number}'

    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return answer, question
