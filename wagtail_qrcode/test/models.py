from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page

from wagtail_qrcode.models import QRCodeMixin


class TestPage(QRCodeMixin, Page):
    pass
