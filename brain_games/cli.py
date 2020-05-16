"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import prompt


def welcome_user():
    """
    This is an example script.

    It seems that it has to have THIS docstring with a summary line, a blank line
    and sume more text like here. Wow.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
