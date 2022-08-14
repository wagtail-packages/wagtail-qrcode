from django.conf import settings
from django.core.mail import EmailMessage
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail import hooks
else:
    from wagtail.core import hooks

from wagtail.documents import get_document_model

from wagtail_qrcode.cls import WagtailQrCode, create_collection


@hooks.register("after_create_page")
@hooks.register("after_edit_page")
def generate_qr_code(request, page):
    """Add a QR code to the page."""

    collection = create_collection("QR Codes")

    qrc = WagtailQrCode(page, collection)

    svg, document = qrc.build()

    page.qr_code_svg = svg
    page.qr_code_eps = document

    rev = page.save_revision()
    rev.publish()


def send_qr_code_email(page, email=None, subject=None, body=None):
    """Send the QR code to the email address."""
    # need to add some error logging here
    # see mailhog `jim` setting, he messes things up and make errors fo you.
    doc = page.qr_code_eps
    if doc is None or email is None:
        return

    if subject is None:
        subject = f"QR Code for {page.title}"
    if body is None:
        body = f"QR Code for {page.title}"

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
        attachments=[("qr-code-{}.eps".format(page.id), doc.file.read(), "image/eps")],
    )
    try:
        email.send()
    except Exception as e:
        print(e)


@hooks.register("after_delete_page")
def delete_document(request, page):
    doc = get_document_model().objects.filter(id=page.qr_code_eps.id)
    if doc:
        doc.delete()
