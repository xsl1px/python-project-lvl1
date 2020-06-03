"""Main function script."""

from brain_games.games.brain_gcd_game import run
from brain_games.greetings import greeting_brain_gcd


def main():
    """Run main function."""
    greeting_brain_gcd()
    run()


if __name__ == '__main__':
    main()
