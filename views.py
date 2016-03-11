from __future__ import unicode_literals

from django.views.generic import TemplateView

class AdminView(TemplateView):
    template_name = 'duck_admin/home.html'