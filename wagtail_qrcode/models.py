from django import forms
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents import get_document_model
from wagtail.images import get_image_model

from wagtail_qrcode.field_panels import QrCodeFieldPanel, QrCodeUsageFieldPanel

ImageModel = get_image_model()
DocumentModel = get_document_model()


class QRCodeMixin(models.Model):
    GENERATE_QR_CODE = True

    qr_code_svg = models.TextField(
        verbose_name="QR Code SVG",
        blank=True,
        null=True,
    )

    qr_code_eps = models.ForeignKey(
        get_document_model(),
        verbose_name="QR Code EPS",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    qr_code_usage = models.IntegerField(
        verbose_name="QR Code Usage Count",
        default=0,
    )

    class Meta:
        abstract = True

    panels = [
        QrCodeFieldPanel(
            "qr_code_svg",
            widget=forms.HiddenInput(),
        ),
        QrCodeUsageFieldPanel(
            "qr_code_usage",
            widget=forms.HiddenInput(),
        ),
        FieldPanel("qr_code_eps"),
    ]
