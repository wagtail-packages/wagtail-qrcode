# Using with Wagtail 2.15 or 2.16

This document demonstrate how when using Wagtail version earlier the v3 there are some extra changes to make.

## Using the QRCode page model mixin

Use the model mixin in a new or an existing page model.

```python

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.documents.edit_handlers import DocumentChooserPanel

from wagtail_qrcode.field_panels import QrCodeFieldPanel, QrCodeUsageFieldPanel
from wagtail_qrcode.models import QRCodeMixin

class QRCodePage(QRCodeMixin, Page):
    # your model fields ...

    qrcode_panels = [
        QrCodeFieldPanel(
            "qr_code_svg",
            widget=forms.HiddenInput(),
        ),
        QrCodeUsageFieldPanel(
            "qr_code_usage",
            widget=forms.HiddenInput(),
        ),
        DocumentChooserPanel("qr_code_eps"),
        MultiFieldPanel(
            [
                FieldPanel("qr_code_eps_email"),
            ],
            heading="Email address to send the QR code EPS file to",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
            ObjectList(qrcode_panels, heading="QR Code", classname="qr-code"),
        ]
    )
```

This will add a new tab in the page editor `QR Code` where you can preview the generated QR code and access the downloadable print ready EPS file. (the file can also be found in the documents app)
