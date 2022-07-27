poetry:
	poetry install

test:
	poetry run python testmanage.py test

lint:
	pre-commit run --all-files

add:
	git add .

commit:
	git commit
