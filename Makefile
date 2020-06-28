install:
	poetry install
	#poetry add prompt

lint:
	poetry run flake8 brain_games
	
check:	selfcheck test script

.PHONY: install test script selfcheck check build
