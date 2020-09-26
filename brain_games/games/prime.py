"""Main Game Prime code."""
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    """Function generates random number from 1 to 100."""
    min_number = 1
    max_number = 100
    num = random.randint(min_number, max_number)  # noqa: S311
    global div
    div = 2
    while num % div != 0:
        div += 1

    question = f'{num}'
    answer = 'yes' if isPrime(num) else 'no'
    return answer, question


def get_result():
    """Function returns result for engine.py from isPrime function."""
    return generate_number()


def isPrime(number):
    """Checks if random number from generate_number function is prime."""
    return div == number
