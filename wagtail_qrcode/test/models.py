from wagtail.models import Page

from wagtail_qrcode.models import QRCodeMixin


class TestPage(QRCodeMixin, Page):
    pass
