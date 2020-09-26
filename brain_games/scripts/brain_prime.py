"""Main function script."""

from brain_games.engine import play
from brain_games.games import prime


def start():
    """Run main function."""
    play(prime)


if __name__ == '__main__':
    start()
