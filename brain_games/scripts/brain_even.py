"""Main function script."""

from brain_games.games.brain_even_game import run
from brain_games.greetings import greeting_brain_even


def main():
    """Run main function."""
    greeting_brain_even()
    run()


if __name__ == '__main__':
    main()
