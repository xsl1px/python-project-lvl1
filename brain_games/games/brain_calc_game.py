"""Main random number script code."""
import random
import prompt

import operator


def run():
    """Run main function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    def expression():
        count = 0

        op_list = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        while count != 3:
            num1 = random.randint(1, 100)  # noqa: S311
            num2 = random.randint(1, 100)  # noqa: S311
            op_random = random.choice(['+', '-', '*'])  # noqa: S311
            answer = op_list[op_random](num1, num2)
            print(f'Question: {num1} {op_random} {num2}')
            answer_input = prompt.string('Your answer: ')
            if int(answer_input) == answer:
                print('Correct!')
                count += 1
            else:
                print(f"{answer_input} is wrong answer ;(. Correct answer was {answer}.\nLet's try again, {name}!")
                break
        else:
            print('Congratulations, {0}!'.format(name))

    expression()
