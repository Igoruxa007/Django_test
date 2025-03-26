run:
	poetry run python manage.py runserver

shell:
	poetry run python manage.py shell_plus

migrate:
	poetry run python manage.py migrate

type:
	poetry run mypy .

style:
	poetry run flake8 .
