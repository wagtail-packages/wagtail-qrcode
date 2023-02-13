from django.test import TestCase

from wagtail_qrcode.apps import WagtailQrcodeAppConfig


class TestApps(TestCase):
    def test_config(self):
        self.assertEqual(WagtailQrcodeAppConfig.name, "wagtail_qrcode")
        self.assertEqual(WagtailQrcodeAppConfig.verbose_name, "Wagtail qrcode")
        self.assertEqual(WagtailQrcodeAppConfig.label, "wagtail_qrcode")
