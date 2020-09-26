"""Main number progression game code."""
import random
import copy

DESCRIPTION = 'What number is missing in the progression?'


def get_result():
    """Function returns result for engine.py from find_number_in_progression function."""
    return find_number_in_progression()


def find_number_in_progression():
    """Function generates progression with random numbers and random step."""
    list_progression = []
    len_progression_max = 10  # recommended progression lenght

    while len(list_progression) < len_progression_max:

        first_progression_number = random.randint(0, 1)  # random number from 0 to 1
        last_progression_number = random.randint(first_progression_number + 1, 150)  # random number from first_progression_number + 1 to 150
        progression_step = random.randint(2, 10)  # random number from 2 to 10

        for number in range(first_progression_number, last_progression_number, progression_step):
            list_progression.append(number)

        if len(list_progression) < len_progression_max:
            list_progression = []
            continue

        list_progression = list_progression[0:len_progression_max]  # noqa: WPS349
        random_list_element = random.randint(0, len_progression_max)
        list_copy = copy.copy(list_progression)
        list_progression[random_list_element] = str('..')
        question = (('{} ' * len(list_progression)).format(*list_progression))  # noqa: WPS336, P103
        answer = str(list_copy[random_list_element])
        return answer, question
