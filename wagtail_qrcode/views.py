from django.http import Http404, HttpResponseRedirect
from wagtail.models import Page


def qr_code_page_view(request):
    """QR code redirect view."""
    try:
        page_id = int(request.GET.get("id"))
    except ValueError:
        raise Http404
    except TypeError:
        raise Http404

    try:
        page = Page.objects.get(id=page_id).specific()
    except Page.DoesNotExist:
        raise Http404

    if hasattr(page, "qr_code_usage"):
        page.qr_code_usage += 1
        page.save()

    return HttpResponseRedirect(page.url)
