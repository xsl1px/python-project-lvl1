"""Main number progression script code."""
import random

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    """Game logic function."""  # noqa: DAR201
    def isprime(num):
        div = 2
        while num % div != 0:
            div += 1
        return div == num

    num = random.randint(1, 100)  # noqa: S311
    question = f'Question: {num}'

    if isprime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'

    return answer, question
