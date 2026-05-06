from django.contrib.auth.forms import AuthenticationForm

class LoginContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = AuthenticationForm()
        form.fields['username'].widget.attrs.update({'placeholder': 'username'})
        form.fields['password'].widget.attrs.update({'placeholder': 'password'})
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control form-control-sm'})
        context['login_form'] = form
        return context
