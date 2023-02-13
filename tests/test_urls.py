from django.test import TestCase
from django.urls.resolvers import RoutePattern

from wagtail_qrcode.urls import urlpatterns


class TestUrls(TestCase):
    def test_url_patterns(self):
        path = urlpatterns[0]
        self.assertEqual(path.name, "qr_code_page_view")
        self.assertIsInstance(path.pattern, RoutePattern)
        self.assertEqual(path.callback.__name__, "qr_code_page_view")
