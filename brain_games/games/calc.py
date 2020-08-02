"""Main random number script code."""
import operator
import random


DESCRIPTION = 'What is the result of the expression?'


def logic():
    """Game logic function."""
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    num1 = random.randint(1, 100)  # noqa: S311
    num2 = random.randint(1, 100)  # noqa: S311
    operation_random = random.choice(['+', '-', '*'])  # noqa: S311
    question = f'{num1} {operation_random} {num2}'
    answer = str(operations[operation_random](num1, num2))

    return answer, question
