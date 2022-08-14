from django.test import TestCase

from wagtail_qrcode.test.models import TestPage


class TestModels(TestCase):
    def test_qrcode_mixin(self):
        test_page = TestPage()

        self.assertTrue(hasattr(test_page, "GENERATE_QR_CODE"))
        self.assertTrue(test_page.GENERATE_QR_CODE, True)

        self.assertTrue(hasattr(test_page, "qr_code_svg"))
        self.assertTrue(hasattr(test_page, "qr_code_eps"))
        self.assertTrue(hasattr(test_page, "qr_code_usage"))

        panels = test_page.panels

        self.assertTrue(len(panels) >= 3)
