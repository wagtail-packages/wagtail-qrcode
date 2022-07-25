from django.http import HttpResponseNotFound, HttpResponseRedirect
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page


def qr_code_page_view(request):
    """QR code redirect view."""
    page_id = int(request.GET.get("id"))

    try:
        specific_cls = Page.objects.get(id=page_id).specific_class
        page = specific_cls.objects.get(id=page_id)
    except Page.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    if hasattr(page, "qr_code_usage"):
        page.qr_code_usage += 1
        page.save()
        return HttpResponseRedirect(page.url)

    return HttpResponseNotFound("Page not found")
