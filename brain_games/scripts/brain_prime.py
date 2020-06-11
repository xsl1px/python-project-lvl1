"""Main function script."""

from brain_games.games.brain_prime_game import run
from brain_games.greetings import greeting_brain_prime


def main():
    """Run main function."""
    greeting_brain_prime()
    run()


if __name__ == '__main__':
    main()
