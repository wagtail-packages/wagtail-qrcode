from wagtail.admin.panels import FieldPanel


class QrCodeFieldPanel(FieldPanel):
    class BoundPanel(FieldPanel.BoundPanel):
        template_name = "wagtail_qrcode/admin/field_panel_4.html"


class QrCodeUsageFieldPanel(FieldPanel):
    class BoundPanel(FieldPanel.BoundPanel):
        template_name = "wagtail_qrcode/admin/usage_field_panel_4.html"
