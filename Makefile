install:
	poetry install
	poetry add prompt

make lint:
	poetry run flake8 brain_games