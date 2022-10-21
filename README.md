# Wagtail qrcode

This package can be used to create a page in Wagtail CMS that has a corresponding QR Code.

![Alt text](docs/sample.png?raw=true "Title")

## Features

- The generated QR Code is saved as an EPS document that can be printed then scanned and will link to the page via the page ID
- You can download the generated QR code and use it in printed advertising like posters, postcards, banners, beer mats and more.
- When saving a draft or publishing a page you can add a one-time email address to send the qr-code to as an attachment.

## Installation

To add the package to your own Wagtail CMS

**Install the package into your environment.**

```bash
pip install wagtail-qrcode
```

**Add the package to your site settings.**

```python
INSTALLED_APPS = [
    # ...
    "wagtail_qrcode",
    # ...
]
```

**Add this setting to your Wagtail settings.**

It is used to generate the base url for the QR code

```python
WAGTAIL_QR_CODE_BASE_URL = "your-site-url"
```

## Using the QRCode page model mixin

Use the model mixin in a new or an existing page model.

```python
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.models import Page

from wagtail_qrcode.admin_forms import QrCodeEmailForm
from wagtail_qrcode.models import QRCodeMixin


class QRCodePage(QRCodeMixin, Page):

    qrcode_panels = QRCodeMixin.panels + [
        MultiFieldPanel(
            [
                FieldPanel("email_address"),
                FieldPanel("email_subject"),
                FieldPanel("email_body"),
            ],
            heading="Send QR code via email",
        )
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
            ObjectList(qrcode_panels, heading="QR Code", classname="qr-code"),
        ]
    )

    base_form_class = QrCodeEmailForm
```

This will add a new tab in the page editor `QR Code` where you can preview the generated QR code and access the downloadable print ready EPS file. (the file can also be found in the documents app)

## Wagtail QRCode URLS

Include the wagtail-qrcode urls in your site urls.

The url provides the redirect endpoint for when the qr-code is scanned and viewed in a browser.

```python
urlpatterns = [
    # ...
    path("qr-code/", include("wagtail_qrcode.urls")),
    # ...
]
```

or import the view and pass the view in the path function

```python
from wagtail_qrcode.views import qr_code_page_view

urlpatterns = [
    # ...
    path("qr-code/", qr_code_page_view, name="qr-code-view"),
    # ...
]
```

## Configuration

Set the configuration (optional, these are the defaults)

```python
WAGTAIL_QR_CODE = {
    "collection_name": "QR Codes",
    "scale": 3,
    "quiet_zone": 6,
    "svg_has_xml_declaration": False,
    "svg_has_doc_type_declaration": False,
}
```

- collection_name: is automatically created and used as the collection for all generated QR codes
- scale: the size of the dots in the QR code
- quiet_zone: the plain border around the QR code
- svg_has_xml_declaration: does the QR code SVG have an XML declaration
- svg_has_doc_type_declaration: does the QR code SVG have an HTML doc-type

## Contributing

If you would like to suggest an improvement to the package we welcome [contributions](docs/contrubute.md)

## Issues

If you find an issue or error please consider [raising and issue](https://github.com/nickmoreton/wagtail-qrcode/issues)
