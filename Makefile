.PHONY: all lint migrate test run

migrate:
	python sandbox/manage.py migrate

admin:
	echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin', '', 'changeme')" | python sandbox/manage.py shell

run:
	python sandbox/manage.py runserver 0.0.0.0:8000

test:
	python testmanage.py test

setup:
	python sandbox/manage.py setup

mail:
	cp bin/settings/local.py sandbox/settings/local.py
	docker run -p 8025:8025 -p 1025:1025 mailhog/mailhog

all: migrate admin setup
