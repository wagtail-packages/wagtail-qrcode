from wagtail.admin.panels import FieldPanel


class QrCodeSVGFieldPanel(FieldPanel):
    class BoundPanel(FieldPanel.BoundPanel):
        object_template_name = "wagtail_qrcode/admin/qr_code_svg_field_panel.html"


class QrCodeSVGUsageFieldPanel(FieldPanel):
    class BoundPanel(FieldPanel.BoundPanel):
        object_template_name = "wagtail_qrcode/admin/qr_code_svg_usage_field_panel.html"
