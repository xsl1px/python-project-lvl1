"""Main random number script code."""
import random
import math
from brain_games.engine import string_question

description = 'Find the greatest common divisor of given numbers.'


def play_game():
    """Game logic function."""  # noqa: DAR201
    num1 = random.randint(1, 100)  # noqa: S311
    num2 = random.randint(1, 100)  # noqa: S311
    question = f'{string_question}{num1} {num2}'
    answer = str(math.gcd(num1, num2))
    return answer, question
