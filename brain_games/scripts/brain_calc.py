"""Main function script."""

from brain_games.engine import start
from brain_games.games import brain_calc_game


def main():
    """Run main function."""
    start(brain_calc_game)


if __name__ == '__main__':
    main()
