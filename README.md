# Wagtail qrcode

## Under development

This package can be used to create a page in Wagtail CMS that has a corresponding QR Code.

The generated QR Code is saved as an EPS document that can be printed then scanned and will link to the page.

You can download the generated QR code and use it in printed advertising like posters, postcards, banners, beer mats and more.

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

## Using the QRCode page model mixin

Add the model mixin to a new or an existing page model.

```python
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

## Configuration

Set the base url for the generated QR code

```python
WAGTAILADMIN_BASE_URL = "http://example.com"
```

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

**Create the development app** (requires poetry environment ^^ to be activated)

```bash
develop
```

and run the following

```bash
make all
```

This will install a Wagtail app that can be used to develop the package. The app can be viewed at <http://localhost:8000>

You can log into the admin at <http://localhost:8000/admin> and use `admin` for the username & `changeme` for the password.

### Other commands

You can use the commands in the Make file to conveininetly run various commands.

- `make migrate` run migrations
- `make run` run the development server
- `make test` run the tests

Although it not required as the sandbox app is ignored by git you can remove the development app by running.

```bash
clean
```
