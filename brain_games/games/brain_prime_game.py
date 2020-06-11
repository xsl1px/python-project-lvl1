"""Main number progression script code."""
import random
import prompt


def run():
    """Run main function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    def isprime(num):
        div = 2
        while num % div != 0:
            div += 1
        return div == num

    count = 0
    while count != 3:
        num = random.randint(1, 100)  # noqa: S311
        print(f'Question: {num}')
        answer_input = prompt.string('Your answer: ')

        if isprime(num) is True and answer_input == 'yes':
            print('Correct!')
            count += 1
        elif isprime(num) is False and answer_input == 'no':
            print('Correct!')
            count += 1
        elif isprime(num) is True and answer_input == 'no':
            print(f'{answer_input} is wrong answer ;(. Correct answer was "yes"!')
            break
        else:
            print(f'{answer_input} is wrong answer ;(. Correct answer was "no"!')
            break
    else:
        print('Congratulations, {0}!'.format(name))
