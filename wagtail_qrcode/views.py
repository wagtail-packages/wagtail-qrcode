from django.http import Http404, HttpResponseRedirect
from wagtail.core.models import Page


def qr_code_page_view(request):
    """QR code reirect view."""

    try:
        page = Page.objects.get(id=int(request.GET.get("id")))
        url = request.build_absolute_uri(page.url)
        return HttpResponseRedirect(url)
    except Page.DoesNotExist:
        raise Http404("Page does not exist")
