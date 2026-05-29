from django.contrib.auth.forms import AuthenticationForm


class LoginContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_form"] = AuthenticationForm()
        return context
