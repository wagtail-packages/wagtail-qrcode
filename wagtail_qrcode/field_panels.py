from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import FieldPanel
else:
    from wagtail.admin.edit_handlers import FieldPanel


class QrCodeFieldPanel(FieldPanel):
    if WAGTAIL_VERSION >= (4, 0):

        class BoundPanel(FieldPanel.BoundPanel):
            template_name = "wagtail_qrcode/admin/field_panel_4.html"

    elif WAGTAIL_VERSION >= (3, 0):

        class BoundPanel(FieldPanel.BoundPanel):
            object_template_name = "wagtail_qrcode/admin/field_panel.html"

    else:

        object_template = "wagtail_qrcode/admin/field_panel.html"


class QrCodeUsageFieldPanel(FieldPanel):
    if WAGTAIL_VERSION >= (4, 0):

        class BoundPanel(FieldPanel.BoundPanel):
            template_name = "wagtail_qrcode/admin/usage_field_panel_4.html"

    elif WAGTAIL_VERSION >= (3, 0):

        class BoundPanel(FieldPanel.BoundPanel):
            object_template_name = "wagtail_qrcode/admin/usage_field_panel.html"

    else:

        object_template = "wagtail_qrcode/admin/usage_field_panel.html"
