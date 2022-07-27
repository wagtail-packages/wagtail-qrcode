from django.urls import path

from .views import qr_code_page_view

urlpatterns = [
    path("", qr_code_page_view, name="qr_code_page_view"),
]
