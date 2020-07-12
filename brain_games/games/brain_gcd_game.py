"""Main random number script code."""
import random
import math

description = 'Find the greatest common divisor of given numbers.'


def game():
    """Game logic function."""  # noqa: DAR201
    num1 = random.randint(1, 100)  # noqa: S311
    num2 = random.randint(1, 100)  # noqa: S311
    question = f'Question: {num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return answer, question
