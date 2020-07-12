"""Greeting and name prompt functions."""
import prompt


def start(game_name):
    """Engine's welcome code."""  # noqa: DAR101
    print('Welcome to the Brain Games!')
    print(game_name.description)
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    count = 0

    while count != 3:
        answer, question = game_name.game()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                """'{ua}' is wrong answer ;(. Correct answer was '{ca}'
                """.format(ua=user_answer, ca=answer)  # noqa: C813
            )
            print("Let's try again, {n}!".format(n=name))
            break
    if count == 3:
        print('Congratulations, {n}!'.format(n=name))