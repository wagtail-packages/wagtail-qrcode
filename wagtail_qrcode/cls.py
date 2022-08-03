import io

import pyqrcode
from django.conf import settings
from django.core.files.base import File

# from django.core.mail import EmailMessage
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Collection

Document = get_document_model()
Image = get_image_model()


class WagtailQrCode:
    def __init__(self, page, collection=None):
        self.page = page
        # self.content = content
        self.collection = collection

        self.settings = self.settings()

    def settings(self):
        if hasattr(settings, "WAGTAIL_QR_CODE"):
            return settings.WAGTAIL_QR_CODE
        else:
            return {
                "collection_name": "QR Codes",
                "scale": 3,
                "quite_zone": 6,
                "svg_has_xml_declaration": False,
                "svg_has_doc_type_declaration": False,
            }

    def build(self):
        title = self.page.title

        try:
            base_url = settings.WAGTAIL_QR_CODE_BASE_URL
        except AttributeError:
            base_url = settings.WAGTAILADMIN_BASE_URL

        # QR Code instance
        qrc = self.make_qr_code(f"{base_url}/qrcode?id={self.page.id}")

        # SVG QR code
        svg = self.make_svg(qrc)

        # EPS QR code and save a document
        eps = self.make_eps(qrc)
        document = self.make_document(title, eps, self.collection)

        return svg, eps, document

    def make_qr_code(self, content):
        qrc = pyqrcode.create(content)
        return qrc

    def make_svg(self, qrc):
        svg_io = io.BytesIO()
        qrc.svg(
            svg_io,
            scale=self.settings["scale"],
            quiet_zone=self.settings["quite_zone"],
            xmldecl=self.settings["svg_has_xml_declaration"],
            svgns=self.settings["svg_has_doc_type_declaration"],
            title=self.page.title,
        )
        svg_io = svg_io.getvalue().decode()

        return svg_io

    def make_eps(self, qrc):
        eps_io = io.StringIO()
        qrc.eps(
            eps_io,
            scale=self.settings["scale"],
            quiet_zone=self.settings["quite_zone"],
        )

        return eps_io

    def make_document(self, title, eps, collection):
        doc = Document.objects.filter(title=title).first()

        if doc:
            # remove the document to create a replacement
            doc.delete()

        doc = Document(
            title=title,
            file=File(eps, name=f"qr-code-{self.page.id}.eps"),
            collection=collection,
        )
        doc.save()

        return doc


def create_collection(name):
    """Create a collection for the QR codes."""

    try:
        collection = Collection.objects.get(name=name)
    except Collection.DoesNotExist:
        root_collection = Collection.get_first_root_node()
        collection = root_collection.add_child(name=name)

    return collection


# class WagtailQrCode:
#     def __init__(self, page=None, content=None, collection=None):

#         if page is None or content is None:
#             raise AttributeError(
#                 "Page parameter and content parameter are both required"
#             )

#         self.page = page
#         self.content = content

#         # SETTINGS
#         if hasattr(settings, "WAGTAIL_QR_CODE"):
#             self.settings = settings.WAGTAIL_QR_CODE
#         else:
#             self.settings = {
#                 "collection_name": "QR Codes",
#                 "scale": 3,
#                 "quite_zone": 6,
#                 "svg_has_xml_declaration": False,
#                 "svg_has_doc_type_declaration": False,
#             }

#         # COLLECTION
#         if collection is not None:
#             self.settings["collection_name"] = collection

#         self.collection_obj = self.create_collection(self.settings)

#         # BASE_URL
#         if hasattr(settings, "WAGTAIL_QR_CODE_BASE_URL"):
#             self.base_url = settings.WAGTAIL_QR_CODE_BASE_URL
#         else:
#             self.base_url = settings.WAGTAILADMIN_BASE_URL

#     def create_qr_code(self):
#         """Create a QR code."""
#         return pyqrcode.create(self.content)

#     @staticmethod
#     def create_collection(settings):
#         """Create a collection for the QR codes."""

#         try:
#             collection = Collection.objects.get(name=settings["collection_name"])
#         except Collection.DoesNotExist:
#             root_collection = Collection.get_first_root_node()
#             collection = root_collection.add_child(name=settings["collection_name"])

#         return collection

#     def document_title(self):
#         """Create a document title."""

#         return f"QR Code for {self.page.title}"

#     @staticmethod
#     def create_document(title, eps, collection):
#         """Create a document for the QR code."""

#         doc = Document.objects.filter(title=title).first()
#         if doc:
#             # remove the document to create a replacement
#             doc.delete()

#         doc = Document(
#             title=title,
#             file=File(eps, name=f"qr-code-{title}.eps"),
#             collection=collection,
#         )
#         doc.save()

#         return doc

#     @staticmethod
#     def create_svg(title, qrc, settings):
#         """Create an SVG file for the QR code."""

#         bytes = io.BytesIO()
#         qrc.svg(
#             bytes,
#             scale=settings["scale"],
#             quiet_zone=settings["quite_zone"],
#             xmldecl=settings["svg_has_xml_declaration"],
#             svgns=settings["svg_has_doc_type_declaration"],
#             title=title,
#         )

#         return bytes.getvalue().decode()

#     @staticmethod
#     def create_eps(qrc, settings):
#         """Create an EPS file for the QR code."""

#         string = io.StringIO()
#         qrc.eps(
#             string,
#             scale=settings["scale"],
#             quiet_zone=settings["quite_zone"],
#         )

#         return string

#     def email_document(self, page):
#         """Send the QR code to the email address."""
#         # need to add some error logging here
#         # see mailhog `jim` setting, he messes things up and make errors fo you.
#         title = self.document_title()

#         email = EmailMessage(
#             subject=title,
#             body=title,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=[page.qr_code_eps_email],
#             attachments=[title, page.qr_code_eps.getvalue()],
#         )

#         return email.send()
