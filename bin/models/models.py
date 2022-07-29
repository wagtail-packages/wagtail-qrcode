from wagtail.admin.panels import ObjectList, TabbedInterface
from wagtail.models import Page

from wagtail_qrcode.models import QRCodeMixin


class HomePage(Page):
    pass


class QRCodePage(QRCodeMixin, Page):

    edit_handler = TabbedInterface(
        [
            ObjectList(Page.content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
            ObjectList(QRCodeMixin.panels, heading="QR Code", classname="qr-code"),
        ]
    )
