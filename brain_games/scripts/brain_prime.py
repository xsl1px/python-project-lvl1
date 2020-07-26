"""Main function script."""

from brain_games.engine import play
from brain_games.games import prime


def main():
    """Run main function."""
    play(prime)


if __name__ == '__main__':
    main()
