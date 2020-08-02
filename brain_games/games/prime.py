"""Main number progression script code."""
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def logic():
    """Game logic function."""  # noqa: DAR201
    num = random.randint(1, 100)  # noqa: S311
    div = 2
    while num % div != 0:
        div += 1

    question = f'{num}'

    if div == num:
        answer = 'yes'
    else:
        answer = 'no'

    return answer, question
