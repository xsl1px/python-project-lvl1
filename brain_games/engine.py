"""Greeting and name prompt functions."""
import prompt

string_question = 'Question: '


def play(game):
    """Engine's welcome code."""  # noqa: DAR101
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    correct_answers_count = 3

    while correct_answers_count != 0:
        answer, question = game.get_result()
        print(string_question + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            correct_answers_count -= 1
        else:
            print(
                """'{ua}' is wrong answer ;(. Correct answer was '{ca}'
                """.format(ua=user_answer, ca=answer)  # noqa: C813
            )
            print("Let's try again, {n}!".format(n=name))
            break
    print('Congratulations, {n}!'.format(n=name))
