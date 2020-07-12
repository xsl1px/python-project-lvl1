"""Main random number script code."""
import operator
import random

description = 'What is the result of the expression?'


def game():
    """Game logic function."""  # noqa: DAR201
    op_list = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    num1 = random.randint(1, 100)  # noqa: S311
    num2 = random.randint(1, 100)  # noqa: S311
    op_random = random.choice(['+', '-', '*'])  # noqa: S311
    question = f'Question: {num1} {op_random} {num2}'
    answer = str(op_list[op_random](num1, num2))

    return answer, question
