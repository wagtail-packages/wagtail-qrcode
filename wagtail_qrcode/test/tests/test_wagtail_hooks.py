import io
import tempfile

import pyqrcode
from django.core.files.base import File
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from wagtail.documents.models import Document
from wagtail.models import Collection, Page

from wagtail_qrcode.test.models import TestPage
from wagtail_qrcode.wagtail_hooks import (
    create_qr_code_document,
    create_qrcode_collection,
    delete_eps_qrcode_from_documents,
    get_base_url,
    get_settings,
    make_qr_code_eps,
    make_svg_qr_code,
)


class TestWagtailHooks(TestCase):
    def test_make_svg_qr_code(self):
        qr_code = pyqrcode.create("http://example.com/qrcode?id=1")
        svg_io = make_svg_qr_code("qr code", qr_code)
        self.assertIsInstance(svg_io, str)

    def test_make_qr_code_eps(self):
        qr_code = pyqrcode.create("http://example.com/qrcode?id=1")
        eps_io = make_qr_code_eps(qr_code)
        self.assertIsInstance(eps_io, io.StringIO)

    def test_create_qr_code_document(self):
        collection = create_qrcode_collection()
        doc = create_qr_code_document(
            page=Page(title="Foo Page"),
            collection=collection,
            eps_io=io.BytesIO(b"foo"),
            document_title="QR Code for Foo Page",
        )
        document = Document.objects.get(title="QR Code for Foo Page")
        self.assertEqual(doc, document)

    def test_create_qrcode_collection(self):
        collection = create_qrcode_collection()
        self.assertIsInstance(collection, Collection)
        self.assertEqual(collection.name, "QR Codes")

    def test_qr_code_settings_default(self):
        expected_settings = {
            "collection_name": "QR Codes",
            "scale": 3,
            "quite_zone": 6,
            "svg_has_xml_declaration": False,
            "svg_has_doc_type_declaration": False,
        }
        self.assertEqual(get_settings(), expected_settings)

    @override_settings(WAGTAIL_QR_CODE={"collection_name": "foo codes"})
    def test_qr_code_settings_overide(self):
        self.assertEqual(get_settings()["collection_name"], "foo codes")

    def test_get_base_url(self):
        request = RequestFactory().get("/")
        self.assertEqual(get_base_url(request), "http://testserver/")

    @override_settings(QRCODE_BASE_URL="http://foo.com/")
    def test_get_base_url_override(self):
        self.assertEqual(get_base_url({}), "http://foo.com/")

    def test_delete_eps_from_documents(self):
        with tempfile.TemporaryFile() as f:
            # make a couple of documents
            f.write(b"content")
            Document(title="Foo", file=File(f, name="foo.eps")).save()
            Document(title="Bar", file=File(f, name="bar.eps")).save()

        self.assertEqual(Document.objects.count(), 2)

        # the document that will be linked to the page
        document_linked = Document.objects.get(title="Foo")

        # add a test page that inherits from QRCodeMixin
        root = Page.objects.get(id=1)
        home_page = root.get_children().first()
        fake_page = TestPage(title="Test Page", qr_code_eps=document_linked)
        home_page.add_child(instance=fake_page)
        rev = fake_page.save_revision()
        rev.publish()

        request = RequestFactory().get("/")

        # delete the eps file linked to fale_page from the documents
        delete_eps_qrcode_from_documents(request, fake_page)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.first().title, "Bar")
