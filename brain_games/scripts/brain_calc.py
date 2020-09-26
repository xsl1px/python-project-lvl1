"""Main function script."""

from brain_games.engine import play
from brain_games.games import calc


def start():
    """Run main function."""
    play(calc)


if __name__ == '__main__':
    start()
