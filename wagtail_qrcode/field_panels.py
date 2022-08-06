from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import FieldPanel
else:
    from wagtail.admin.edit_handlers import FieldPanel


class QrCodeSVGFieldPanel(FieldPanel):
    if WAGTAIL_VERSION >= (3, 0):

        class BoundPanel(FieldPanel.BoundPanel):
            object_template_name = "wagtail_qrcode/admin/qr_code_svg_field_panel.html"

    else:
        object_template_name = "wagtail_qrcode/admin/qr_code_svg_field_panel.html"


class QrCodeSVGUsageFieldPanel(FieldPanel):
    if WAGTAIL_VERSION >= (3, 0):

        class BoundPanel(FieldPanel.BoundPanel):
            object_template_name = (
                "wagtail_qrcode/admin/qr_code_svg_usage_field_panel.html"
            )

    else:
        object_template_name = "wagtail_qrcode/admin/qr_code_svg_usage_field_panel.html"
