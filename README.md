# Wagtail qrcode

## Under development

These are the features not yet completed.

- Counting qr-code scans
- Expand the documentation

---

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/nickmoreton/wagtail-qrcode/main.svg)](https://results.pre-commit.ci/latest/github/nickmoreton/wagtail-qrcode/main)

This package can be used to create a page in Wagtail CMS that has a corresponding QR Code.

The generated QR Code is saved as an EPS document that can be printed then scanned and will link to the page.

You can download the generated QR code and use it in printed advertising like posters, postcards, banners, beer mats and more.

When saving a draft or publishing a page you can add an email address to send the qr-code to as an attachment.

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

**Add this setting to your Wagtail settings.**

It is used to generate the base url for the QR code

```python
WAGTAIL_QR_CODE_BASE_URL = "your-site-site-url"
```

## Using the QRCode page model mixin

Use the model mixin in a new or an existing page model.

```python

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList # Wagtail <= 2.*.*
from wagtail.admin.panels import TabbedInterface, ObjectList # Wagtail >= 3.*.*

from wagtail_qrcode.models import QRCodeMixin

class QRCodePage(QRCodeMixin, Page):
    # other model fields ...

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
            ObjectList(QRCodeMixin.panels, heading="QR Code", classname="qr-code"),
        ]
    )
```

This will add a new tab in the page editor `QR Code` where you can preview the generated QR code and access the downloadable print ready EPS file. (the file can also be found in the documents app)

## Wagtail QRCode URLS

You should include the wagtail-qrcode urls in your site urls.

The url provides the redirect endpoint when the qr-code is scanned.

```python
urlpatterns = [
    ...
    path("qr-code/", include("wagtail_qrcode.urls")),
    ...
]
```

or import the view and pass the view in the path function

```python
from wagtail_qrcode.views import qr_code_page_view

urlpatterns = [
    ...
    path("qr-code/", qr_code_page_view, name="qr-code-view"),
    ...
]
```

## Configuration

Set the configuration (optional, these are the defaults)

```python
WAGTAIL_QR_CODE={
    "collection_name": "QR Codes",
    "scale": 3,
    "quite_zone": 6,
    "svg_has_xml_declaration": False,
    "svg_has_doc_type_declaration": False,
}
```

## Contributing

Development setup

**First clone this repo to your computer.**

```bash
git clone https://github.com/nickmoreton/wagtail-qrcode
```

### Poetry environnment

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
- `make mail` to run a docker container for `MailHog`

Although it not required as the sandbox app is ignored by git you can remove the development app and files by running.

```bash
clean
```

## Testing

The app has django tests and has `tox` setup for running them against the compatible Wagtail and Django versions. Tox testing is also run when pushing branches to GitHub in the GitHub actions scripts.
