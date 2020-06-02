"""Main function script."""

from brain_games.games.brain_calc_game import run
from brain_games.greetings import greeting_brain_calc


def main():
    """Run main function."""
    greeting_brain_calc()
    run()


if __name__ == '__main__':
    main()
