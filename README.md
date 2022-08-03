# Wagtail qrcode

This package can be used to create a page in Wagtail CMS that has a corresponding QR Code that can be printed then scanned and will link to the page.

You can download the generated QR code as a print ready EPS file that can be added to posters, postcards, banners, beer mats and more.

Simply send the QR code to a printer or use the EPS file at an online printing service.

## Under development

Todo:
- [ ] add tests
- [ ] add sandbox app models
- [ ] add documentation

## Installation

To add the package to your own Wagtail CMS

**Install the package into your environment.**

```bash
pip install wagtail-qrcode
```

**Add the package to your site settings.**

```python
INSTALLED_APPS = [
    ...
    "wagtail_qrcode",
    ...
]
```

## CMS setup

- about the page model mixin.
- about the content editor usage.
- about downloading the QR code

## Contributing

Development setup

**First clone this repo to a folder on your computer.**

```bash
git clone https://github.com/nickmoreton/wagtail-qrcode
```

**Use [Poetry](https://python-poetry.org) for dependency installation & environment management.**

```bash
poetry install
poetry shell
```

**Create a development app** (optional & requires poetry environment ^^ to be activated)

```bash
create
```

**Run the development setup**

```bash
make all
```

This will install a Wagtail app that can be used to test your new features. The app can be viewed at <http://localhost:8000>

You can log into the admin at <http://localhost:8000/admin> and use `admin` for the username & `changeme` for the password.

### Other commands

You can use the commands in the Make file to conveininetly run various commands.

- `make migrate` run the django migrations
- `make run` run the django development server
- `make test` run the django tests
- `make admin` create and admin user account. UN: `admin` PW: `changeme`

Although it not required as the sandbox app is ignored by git you can remove the development app by running.

```bash
remove
```
