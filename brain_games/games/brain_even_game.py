"""Main random number script code."""
import random

description = 'Answer "yes" if number even otherwise answer "no".'


def game():
    """Game logic function."""  # noqa: DAR201
    number = random.randint(1, 100)  # noqa: S311
    question = f'Question: {number}'
    if number % 2 == 0:
        return 'yes', question

    elif number % 2 != 0:
        return 'no', question
