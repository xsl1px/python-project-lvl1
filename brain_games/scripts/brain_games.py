"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
from brain_games.cli import welcome_user
#from scripts.brain_even import random_number


#welcome_user()

def main():
    """
    Do This is an example script.

    It seems that it has to have THIS docstring with a summary line
    and sume more text like here. Wow.
    """
    print('Welcome to the Brain Games!')    # noqa: WPS421
    print('Answer "yes" if number even otherwise answer "no".')    # noqa: WPS421

#random_number()

if __name__ == '__main__':
    main()
