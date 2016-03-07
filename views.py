from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# class LoginView(FormView):
#
#     title = _("Please Login")
#     login_form = None
#     login_template = None
#
#     @filter_hook
#     def update_params(self, defaults):
#         pass
#
#     @never_cache
#     def get(self, request, *args, **kwargs):
#         context = self.get_context()
#         helper = FormHelper()
#         helper.form_tag = False
#         context.update({
#             'title': self.title,
#             'helper': helper,
#             'app_path': request.get_full_path(),
#             REDIRECT_FIELD_NAME: request.get_full_path(),
#         })
#         defaults = {
#             'extra_context': context,
#             'current_app': self.admin_site.name,
#             'authentication_form': self.login_form or AdminAuthenticationForm,
#             'template_name': self.login_template or 'xadmin/views/login.html',
#         }
#         self.update_params(defaults)
#         return login(request, **defaults)
#
#     @never_cache
#     def post(self, request, *args, **kwargs):
#         return self.get(request)


class AdminView(TemplateView):
    template_name = 'duck_admin/home.html'