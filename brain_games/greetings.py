"""Greeting and name prompt functions."""

import prompt


def welcome_user():
    """Prompt name function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


def greeting_brain_even():
    """Greeting brain-even function."""
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')


def greeting_brain_calc():
    """Greeting brain_calc function."""
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
