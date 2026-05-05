from django.views.generic import ListView, RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy # what does reverse_lazy do?
from .models import Article

# Create your views here.
class Articles(ListView):
    model = Article
    template_name = 'app/articles.html'
    context_object_name = 'articles'
    queryset = Article.objects.select_related('author').defer('content')


class Home(RedirectView):
    pattern_name = 'app:articles'


class Login(LoginView):
    template_name = 'app/login.html'

    def get_success_url(self):
        return reverse_lazy('app:home')
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
