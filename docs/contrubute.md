# Contributing

Development setup

## First clone this repo to your computer

```bash
git clone https://github.com/nickmoreton/wagtail-qrcode
```

## Poetry environnment

**Use [Poetry](https://python-poetry.org) for dependency installation & environment management.**

```bash
poetry install
poetry shell
```

**Create the development app** (requires poetry environment ^^ to be activated) run the poetry script

```bash
develop
```

To build a development app run

```bash
make all
```

To run the development app

```bash
make run
```

This will create a Wagtail app that can be used to develop the package. The app can be viewed at <http://localhost:8000>

You can log into the admin at <http://localhost:8000/admin> and use `admin` for the username & `changeme` for the password.

### Other commands

You can use the commands in the Make file to conveniently run various commands.

- `make migrate` run migrations
- `make run` run the development server
- `make test` run the tests
- `make admin` to quickly setup a superuser account with the above login details.
- `make run` to run the django development server
- `make test` to run the django tests
- `make lint` to run pre-commit --all-files
- `make coverage` to run a coverage report
- `make mail` to run a [docker container](docs/mailhog.md) for `MailHog`

Although it's not required as the sandbox app and temp files and folders created during testing are ignored by git you can remove these by running.

```bash
clean
```

## Testing

The app has django tests and has `tox` setup for running them against the compatible Wagtail and Django versions.

Tox is also run when pushing branches to GitHub in the GitHub actions scripts.
