"""Main Game GCD code."""
import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_result():
    """Function returns result for engine.py from find_gcd function."""
    return find_gcd()


def find_gcd():
    """Function finds the greatest common divisor between two random numbers."""
    min_number = 1
    max_number = 100

    num1 = random.randint(min_number, max_number)  # noqa: S311
    num2 = random.randint(min_number, max_number)  # noqa: S311
    question = f'{num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return answer, question
