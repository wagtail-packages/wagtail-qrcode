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
	python sandbox/manage.py migrate && python sandbox/manage.py setup

mail:
	cp bin/settings/local.py sandbox/settings/local.py
	docker run -p 8025:8025 -p 1025:1025 mailhog/mailhog

all: migrate test admin setup run

# docker commands
build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down -v

sh:
	docker-compose exec app bash

start:
	docker-compose up -d && docker-compose exec app poetry run make develop && docker-compose exec app poetry run make all

destroy:
	docker-compose up -d && docker-compose exec app poetry run clean
