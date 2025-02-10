run:
	poetry run python manage.py runserver

type:
	poetry run mypy .

style:
	poetry run flake8 .
