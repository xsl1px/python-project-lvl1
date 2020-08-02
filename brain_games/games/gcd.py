"""Main random number script code."""
import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def logic():
    """Game logic function."""
    num1 = random.randint(1, 100)  # noqa: S311
    num2 = random.randint(1, 100)  # noqa: S311
    question = f'{num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return answer, question
