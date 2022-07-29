import io

import pyqrcode
from django.conf import settings
from django.core.files.base import File
from django.core.mail import EmailMessage
from wagtail import hooks
from wagtail.documents import get_document_model
from wagtail.images import get_image_model
from wagtail.models import Collection

Image = get_image_model()
Document = get_document_model()

if not hasattr(settings, "WAGTAIL_QR_CODE"):
    QRCODE_SETTINGS = {
        "collection_name": "QR Codes",
        "scale": 3,
        "quite_zone": 6,
        "svg_has_xml_declaration": False,
        "svg_has_doc_type_declaration": False,
    }
else:
    QRCODE_SETTINGS = settings.WAGTAIL_QR_CODE


@hooks.register("after_create_page")
@hooks.register("after_edit_page")
def generate_qr_code(request, page):
    """Add a QR code to the page."""

    title = page.title
    base_url = get_base_url(request)
    collection = create_qrcode_collection(QRCODE_SETTINGS["collection_name"])

    # QR Code instance
    qrc = pyqrcode.create(f"{base_url}qrcode-redirect?id={page.id}")

    # SVG QR code
    page.qr_code_svg = make_svg_qr_code(title, qrc)

    # EPS QR code
    eps_io = make_qr_code_eps(qrc)
    document_title = f"QR Code for {page.title}"
    page.qr_code_eps = create_qr_code_document(page, collection, eps_io, document_title)

    # send the eps file to the email address
    if page.qr_code_eps_email:
        send_qr_code_email(page, eps_io)
        page.qr_code_eps_email = None

    # save a revision and publish the page
    page.save_revision().publish()


def create_qrcode_collection(name="QR Codes"):
    """Create a collection for the QR codes."""

    try:
        collection = Collection.objects.get(name=name)
    except Collection.DoesNotExist:
        root_collection = Collection.get_first_root_node()
        collection = root_collection.add_child(name=name)

    return collection


def send_qr_code_email(page, eps_io):
    """Send the QR code to the email address."""

    email = EmailMessage(
        subject=f"QR Code for {page.title}",
        body=f"QR Code for {page.title}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[page.qr_code_eps_email],
        attachments=[("qr-code-{}.eps".format(page.id), eps_io.getvalue())],
    )
    email.send()


def create_qr_code_document(page, collection, eps_io, document_title):
    """Create a document for the QR code."""

    doc = Document.objects.filter(title=document_title).first()
    if doc:
        # remove the document to create a replacement
        doc.delete()

    doc = Document(
        title=f"QR Code for {page.title}",
        file=File(eps_io, name=f"qr-code-{page.id}.eps"),
        collection=collection,
    )
    doc.save()
    return doc


def make_qr_code_eps(qrc):
    """Create an EPS file for the QR code."""

    eps_io = io.StringIO()
    qrc.eps(
        eps_io,
        scale=QRCODE_SETTINGS["scale"],
        quiet_zone=QRCODE_SETTINGS["quite_zone"],
    )

    return eps_io


def make_svg_qr_code(title, qrc):
    """Create an SVG file for the QR code."""

    svg_io = io.BytesIO()
    qrc.svg(
        svg_io,
        scale=QRCODE_SETTINGS["scale"],
        quiet_zone=QRCODE_SETTINGS["quite_zone"],
        xmldecl=QRCODE_SETTINGS["svg_has_xml_declaration"],
        svgns=QRCODE_SETTINGS["svg_has_doc_type_declaration"],
        title=title,
    )
    svg_io = svg_io.getvalue().decode()
    return svg_io


def get_base_url(request):
    """Get the base URL for the qr code."""

    if hasattr(settings, "QRCODE_BASE_URL"):
        base_url = settings.QRCODE_BASE_URL
    else:
        base_url = request.build_absolute_uri("/")
    return base_url


@hooks.register("after_delete_page")
def delete_eps_qrcode_from_documents(request, page):
    doc = Document.objects.filter(id=page.qr_code_eps.id)
    if doc:
        doc.delete()
