from django.conf import settings
from django.core.management.base import BaseCommand
from sandbox.home.models import QRCodePage
from wagtail.models import Page

from wagtail_qrcode.wagtail_hooks import generate_qr_code


class Command(BaseCommand):
    help = "Create a new page in the sandbox"

    def handle(self, *args, **options):
        root_page = Page.objects.get(id=1)
        home_page = root_page.get_children().first()
        qr_code_page = QRCodePage(title="QR Code Page")
        home_page.add_child(instance=qr_code_page)
        qr_code_page.save_revision().publish()

        settings.QRCODE_BASE_URL = "http://localhost:8000"
        generate_qr_code(None, qr_code_page)
        del settings.QRCODE_BASE_URL
