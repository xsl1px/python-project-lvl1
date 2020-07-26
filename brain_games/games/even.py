"""Main random number script code."""
import random
from brain_games.engine import string_question

description = 'Answer "yes" if number even otherwise answer "no".'


def play_game():
    """Game logic function."""  # noqa: DAR201
    number = random.randint(1, 100)  # noqa: S311
    question = f'{string_question} {number}'
    if number % 2 == 0:
        answer = 'yes'

    elif number % 2 != 0:
        answer = 'no'

    return answer, question
