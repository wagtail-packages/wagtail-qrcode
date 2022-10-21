from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import (
        FieldPanel,
        MultiFieldPanel,
        ObjectList,
        TabbedInterface,
    )
    from wagtail.models import Page
else:
    from wagtail.admin.edit_handlers import (
        FieldPanel,
        MultiFieldPanel,
        ObjectList,
        TabbedInterface,
    )
    from wagtail.core.models import Page

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
