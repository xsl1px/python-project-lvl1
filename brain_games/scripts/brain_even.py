"""Main function script."""

from brain_games.engine import play
from brain_games.games import even


def start():
    """Run main function."""
    play(even)


if __name__ == '__main__':
    start()
