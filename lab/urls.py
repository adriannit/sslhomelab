from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proxyhosts", views.proxyhosts, name="proxyhosts"),
    path("dns", views.dns, name="dns"),
    path("dhcp", views.dhcp, name="dhcp"),
    path("ssl", views.ssl, name="ssl"),
    path("logs", views.logs, name="logs"),
]