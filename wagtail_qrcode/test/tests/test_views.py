from django.test import TestCase
from django.test.client import RequestFactory
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page

from wagtail_qrcode.views import qr_code_page_view


class TestViews(TestCase):
    def test_qr_code_view_404(self):
        request = RequestFactory().get("?id=0")
        response = qr_code_page_view(request)
        self.assertContains(response, "Page not found", status_code=404)

    def test_qr_code_view_redirect(self):
        root_page = Page.objects.get(id=1)
        home_page = root_page.get_children().first()

        test_page = Page(title="Test Page")
        home_page.add_child(instance=test_page)

        rev = test_page.save_revision()
        rev.publish()

        request = RequestFactory().get("?id={}".format(test_page.id))
        response = qr_code_page_view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, test_page.url)
