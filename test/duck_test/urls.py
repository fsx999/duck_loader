# coding=utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="duck_test/test.html")),
    url(r"^truc/", TemplateView.as_view(template_name="duck_test/test.html")),
    url(r"^truc/", TemplateView.as_view(template_name="duck_test/test.html"), name="mon_url")
]