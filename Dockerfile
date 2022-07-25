FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install poetry==1.1.14 && poetry install

# RUN pip install -e .[testing]
