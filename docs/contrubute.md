# Contributing

## Development setup

### First clone this repo to your computer

```bash
git clone https://github.com/nickmoreton/wagtail-qrcode
```

## Setup a virtual environment

```bash
pyenv virtualenv wagtail-qrcode && pyenv activate wagtail-qrcode
```

## Install the package into your virtual environment

```bash
pip install -e ".[testing]"
```

## Setup the testing app

```bash
make migrate && make admin && make run
```

The app can be viewed at <http://localhost:8000>

You can log into the admin at <http://localhost:8000/admin> and use `admin` for the username & `admin` for the password.

## Other commands

You can use the commands in the Make file to conveniently run various commands.

- `make migrate` run migrations
- `make run` run the development server
- `make test` run the tests
- `make admin` to quickly setup a superuser account with the above login details.
- `make lint` to run pre-commit --all-files
- `make mail` to run a [docker container](docs/mailhog.md) for `MailHog`

## Testing

The app uses django tests and has `tox` setup for running them against the compatible Wagtail and Django versions.

Run:

```bash
tox
```
