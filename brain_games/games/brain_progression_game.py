"""Main number progression script code."""
import random
import prompt


def run():
    """Run main function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    def progression():
        """Run progression logic function."""
        count = 0
        while count != 3:
            num1 = random.randint(0, 50)  # noqa: S311
            num2 = random.randint(num1 + 1, 150)  # noqa: S311
            num3 = random.randint(1, 10)  # noqa: S311
            list1 = []

            for number in range(num1, num2, num3):
                list1.append(number)
            if len(list1) >= 10:
                list1 = list1[0:10]  # noqa: WPS349
                random_list_element = random.randint(0, 10)  # noqa: S311
                list2 = list(list1)
                list1[random_list_element] = str('..')
                print(('Question: ' + '{} ' * len(list1)).format(*list1))  # noqa: WPS336, P103
                answer_input = prompt.string('Your answer: ')
                if int(answer_input) == list2[random_list_element]:
                    print('Correct!')
                    count += 1
                else:
                    print(f'{answer_input} is wrong answer ;(. Correct answer was {list2[random_list_element]}!')
                    break
            elif len(list1) < 10:
                continue
        else:
            print('Congratulations, {0}!'.format(name))
    progression()
