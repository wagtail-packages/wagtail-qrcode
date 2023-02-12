from django.test import TestCase
from django.test.client import RequestFactory
from wagtail.models import Page

from tests.testapp.models import QRCodePage
from wagtail_qrcode.views import qr_code_page_view


class TestViews(TestCase):
    @classmethod
    def setUpTestData(self):
        self.request_factory = RequestFactory()
        self.root_page = Page.objects.get(id=1)

        home_page = self.root_page.get_children().first()

        self.test_qrcode_page = QRCodePage(title="Test Page")
        home_page.add_child(instance=self.test_qrcode_page)
        rev = self.test_qrcode_page.save_revision()
        rev.publish()

        self.test_wagtail_page = Page(title="Test Page")
        home_page.add_child(instance=self.test_wagtail_page)
        rev = self.test_wagtail_page.save_revision()
        rev.publish()

    def test_qr_code_view_404(self):
        request = self.request_factory.get("?id=0")
        response = qr_code_page_view(request)

        self.assertContains(response, "Page not found", status_code=404)

    def test_qr_code_view_qrcode_page(self):
        request = self.request_factory.get("?id={}".format(self.test_qrcode_page.id))
        response = qr_code_page_view(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.test_qrcode_page.url)

    def test_qr_code_view_not_qrcode_page(self):
        request = self.request_factory.get("?id={}".format(self.test_wagtail_page.id))
        response = qr_code_page_view(request)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, b"Page not found")

    def test_qr_code_view_usage_count(self):
        request = self.request_factory.get(f"?id={self.test_qrcode_page.id}")

        for i in range(1, 10):
            qr_code_page_view(request)
            self.test_qrcode_page.refresh_from_db()
            self.assertEqual(self.test_qrcode_page.qr_code_usage, i)
