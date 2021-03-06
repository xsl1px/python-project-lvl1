"""Main function script."""

from brain_games.engine import play
from brain_games.games import gcd


def start():
    """Run main function."""
    play(gcd)


if __name__ == '__main__':
    start()
