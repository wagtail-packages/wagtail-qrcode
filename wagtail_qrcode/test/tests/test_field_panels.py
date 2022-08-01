from django import forms
from django.test import TestCase

from wagtail_qrcode.field_panels import QrCodeSVGFieldPanel, QrCodeSVGUsageFieldPanel


class TestFieldPanels(TestCase):
    def test_qr_code_svg_field_panel(self):
        fp = QrCodeSVGFieldPanel("foo", widget=forms.TextInput, classname="full")
        fp.field_name = "foo"

    def test_qr_code_svg_usage_field_panel(self):
        fp = QrCodeSVGUsageFieldPanel("bar", widget=forms.TextInput, classname="full")
        fp.field_name = "bar"
