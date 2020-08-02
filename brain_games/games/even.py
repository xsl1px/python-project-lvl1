"""Main random number script code."""
import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def logic():
    """Game logic function."""  # noqa: DAR201
    number = random.randint(1, 100)  # noqa: S311
    question = f'{number}'
    return ('yes', question) if number % 2 == 0 else ('no', question)
