"""Main function script."""

from brain_games.games.brain_progression_game import run
from brain_games.greetings import greeting_brain_progression


def main():
    """Run main function."""
    greeting_brain_progression()
    run()


if __name__ == '__main__':
    main()
