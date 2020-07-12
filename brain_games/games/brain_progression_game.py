"""Main number progression script code."""
import random

description = 'What number is missing in the progression?'


def game():
    """Game logic function."""  # noqa: DAR201
    list1 = []

    while len(list1) < 10:

        num1 = random.randint(0, 1)  # noqa: S311
        num2 = random.randint(num1 + 1, 150)  # noqa: S311
        num3 = random.randint(2, 10)  # noqa: S311

        for number in range(num1, num2, num3):
            list1.append(number)

        if len(list1) < 10:
            list1 = []
            continue

        list1 = list1[0:10]  # noqa: WPS349
        random_list_element = random.randint(0, 10)  # noqa: S311
        list2 = list(list1)
        list1[random_list_element] = str('..')
        question = (('Question: ' + '{} ' * len(list1)).format(*list1))  # noqa: WPS336, P103
        answer = str(list2[random_list_element])
        return answer, question
