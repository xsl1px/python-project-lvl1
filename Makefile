install:
	poetry install
	#poetry add prompt

lint:
	poetry run flake8 brain_games
	
check:	selfcheck test lint

.PHONY: install test lint selfcheck check build
