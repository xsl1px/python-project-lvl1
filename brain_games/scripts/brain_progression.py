"""Main function script."""

from brain_games.engine import play
from brain_games.games import progression


def start():
    """Run main function."""
    play(progression)


if __name__ == '__main__':
    start()
