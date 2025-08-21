from django.http import Http404, HttpResponseRedirect
from wagtail.models import Page


def qr_code_page_view(request):
    """QR code redirect view."""
    page_id = int(request.GET.get("id"))

    try:
        specific_cls = Page.objects.get(id=page_id).specific_class
        page = specific_cls.objects.get(id=page_id)
    except Page.DoesNotExist:
        raise Http404

    if hasattr(page, "qr_code_usage"):
        page.qr_code_usage += 1
        page.save()

    return HttpResponseRedirect(page.url)
