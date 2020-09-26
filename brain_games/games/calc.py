"""Main Game Calculate code."""
import operator
import random

DESCRIPTION = 'What is the result of the expression?'


def get_result():
    """Returns result for engine.py from calculate function."""
    return calculate()


def calculate():
    """Calculates random operation with two random numbers from 1 to 100."""
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    min_number = 1
    max_number = 100

    num1 = random.randint(min_number, max_number)  # noqa: S311
    num2 = random.randint(min_number, max_number)  # noqa: S311
    operation = random.choice(['+', '-', '*'])  # noqa: S311

    global answer, question
    question = f'{num1} {operation} {num2}'
    answer = str(operations[operation](num1, num2))
    return answer, question
