import sys

from django.apps import AppConfig
from django.conf import settings

warning = """
*****************************************
** WAGTAIL_QR_CODE_BASE_URL is not set **
*****************************************

"""


class WagtailQrcodeAppConfig(AppConfig):
    label = "wagtail_qrcode"
    name = "wagtail_qrcode"
    verbose_name = "Wagtail qrcode"

    def ready(self):
        if not hasattr(settings, "WAGTAIL_QR_CODE_BASE_URL"):
            sys.stderr.write(warning)
            exit(1)
