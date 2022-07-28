.PHONY: all lint migrate test run

migrate:
	python manage.py migrate

admin:
	echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', '', 'changeme')" | python manage.py shell

run:
	python manage.py runserver

test:
	python manage.py test

all: migrate test admin run
