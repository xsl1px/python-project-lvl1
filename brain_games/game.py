import random
import prompt
#from brain_games.cli import welcome_user




def run():

    def greet():
        """
        Do This is an example script.

        It seems that it has to have THIS docstring with a summary line
        and sume more text like here. Wow.
        """
        print('Welcome to the Brain Games!')    # noqa: WPS421
        print('Answer "yes" if number even otherwise answer "no".')    # noqa: WPS421
    greet()

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421


    def random_number():
        a = 0
        while a != 3:
            number = random.randint(1, 100)
            print('Question: ' + str(number))  # noqa: WPS421
            answer = prompt.string('Your answer: ')  # noqa: WPS421
            
            
            if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
                print("Correct!")  # noqa: WPS421
                a += 1
            elif number % 2 == 0 and answer == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {0}!".format(name))  # noqa: WPS421
                break
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {0}!".format(name))  # noqa: WPS421
                break
        else:
            print("Congratulations, {0}!".format(name))  # noqa: WPS421
            #break

    random_number()
