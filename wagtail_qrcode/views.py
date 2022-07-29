from django.http import HttpResponseNotFound, HttpResponseRedirect
from wagtail.core.models import Page


def qr_code_page_view(request):
    """QR code reirect view."""

    try:
        page = Page.objects.get(id=int(request.GET.get("id")))
        # url = request.build_absolute_uri(page.url)
        return HttpResponseRedirect(page.url)
    except Page.DoesNotExist:
        return HttpResponseNotFound("Page not found")
