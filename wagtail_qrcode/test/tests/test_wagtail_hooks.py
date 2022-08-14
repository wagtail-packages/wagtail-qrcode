from django.conf import settings
from django.core import mail
from django.test import RequestFactory, TestCase
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.documents import get_document_model

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page

from wagtail_qrcode.test.models import TestPage
from wagtail_qrcode.wagtail_hooks import (
    delete_document,
    generate_qr_code,
    send_qr_code_email,
)


class TestWagtailHooks(TestCase):
    def test_generate_qr_code(self):
        request = RequestFactory().get("/")
        page = TestPage(title="Test Page")

        self.assertEqual(page.qr_code_svg, None)
        self.assertEqual(page.qr_code_eps, None)
        self.assertEqual(page.qr_code_usage, 0)

        root_page = Page.objects.get(id=1)
        home_page = root_page.get_children().first()
        home_page.add_child(instance=page)

        rev = page.save_revision()
        rev.publish()

        test_page = TestPage.objects.get(id=page.id)

        generate_qr_code(request, test_page)

        self.assertEqual(test_page.qr_code_svg[:4], "<svg")
        self.assertEqual(test_page.qr_code_eps.id, 1)
        self.assertEqual(test_page.qr_code_usage, 0)

        rev = test_page.save_revision()
        rev.publish()

        send_qr_code_email(
            test_page,
            email="foo@bar.com",
            subject="QR Code for Test Page",
            body="QR Code for Test Page",
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "QR Code for Test Page")
        self.assertEqual(mail.outbox[0].body, "QR Code for Test Page")
        self.assertEqual(mail.outbox[0].from_email, settings.DEFAULT_FROM_EMAIL)
        self.assertEqual(mail.outbox[0].to, ["foo@bar.com"])
        self.assertEqual(
            mail.outbox[0].attachments[0][0], "qr-code-{}.eps".format(test_page.id)
        )

        delete_document(request, test_page)
        self.assertEqual(get_document_model().objects.count(), 0)
