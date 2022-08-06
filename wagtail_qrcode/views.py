from django.http import HttpResponseNotFound, HttpResponseRedirect
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page


def qr_code_page_view(request):
    """QR code reirect view."""

    try:
        page = Page.objects.get(id=int(request.GET.get("id")))
        return HttpResponseRedirect(page.url)
    except Page.DoesNotExist:
        return HttpResponseNotFound("Page not found")
