"""Main number progression script code."""
import random
import copy
from brain_games.engine import string_question

description = 'What number is missing in the progression?'


def play_game():
    """Game logic function."""  # noqa: DAR201
    list_progression = []

    while len(list_progression) < 10:

        num1 = random.randint(0, 1)  # noqa: S311
        num2 = random.randint(num1 + 1, 150)  # noqa: S311
        num3 = random.randint(2, 10)  # noqa: S311

        for number in range(num1, num2, num3):
            list_progression.append(number)

        if len(list_progression) < 10:
            list_progression = []
            continue

        list_progression = list_progression[0:10]  # noqa: WPS349
        random_list_element = random.randint(0, 10)  # noqa: S311
        list_copy = copy.copy(list_progression)
        list_progression[random_list_element] = str('..')
        question = ((string_question + '{} ' * len(list_progression)).format(*list_progression))  # noqa: WPS336, P103
        answer = str(list_copy[random_list_element])
        return answer, question
