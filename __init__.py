# coding=utf-8
import sys
from django.conf.urls import url, include
from duck_loader import views
from django.apps import apps
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views

def init_bo_url():
    """
    Initialisation des urls du backoffice
    fonction lisant l'attribut url des AppConfigs et forme les inclusions
    :return: urlpartterns (liste d'url des insclusions des applications
    :rtype: urlpartterns
    """

    bo_url = []

    for x in apps.get_app_configs():
        if getattr(x, 'url', None):
            bo_url.append(url(x.url['regex'], staff_member_required(include("{}.{}".format(x.module.__name__, x.url['module_url'])))))
    urlpatterns = [
        url(r'^$', staff_member_required(views.AdminView.as_view(), login_url='duck_loader:login')),
        url(r'^login/$', auth_views.login, {"template_name": 'duck_admin/auth/login.html'}, name="login")
    ]
    urlpatterns += bo_url
    urlpatterns = [url(r'^', include(urlpatterns, namespace='duck_loader'))]  # ajout du namespace pour eviter les multi login et autres des autres application
    return urlpatterns


def init_webapi_url():
    """
    Initialisation des urls des webapi
    fonction lisant l'attribut url des AppConfigs et forme les inclusions
    :return: urlpartterns (liste d'url des insclusions des applications
    :rtype: urlpartterns
    """
    webapi_url = []

    for x in apps.get_app_configs():
        if getattr(x, 'webapi_url', None):
            webapi_url.append(url(x.url['regex'], include("{}.{}".format(x.module.__name__, x.url['module_url']))))

    urlpatterns = [
        url(r'^$', views.AdminView.as_view())
    ]

    urlpatterns += webapi_url
    return urlpatterns