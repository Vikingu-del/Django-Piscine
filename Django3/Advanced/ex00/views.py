from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, RedirectView, CreateView, DetailView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy # what does reverse_lazy do?
from .models import Article, UserFavouriteArticle

# Create your views here.
class Articles(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'ex00/articles.html'
    context_object_name = 'articles'
    queryset = Article.objects.select_related('author').defer('content')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['favorite_ids'] = set(UserFavouriteArticle.objects.filter(
                user=self.request.user
            ).values_list('article_id', flat=True))
        return context
         
        


class Publications(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'ex00/publications.html'
    context_object_name = 'articles'
    login_url = '/login/'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).defer('content', 'author').all()


class Favourites(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = 'ex00/favourites.html'
    context_object_name = 'articles'
    login_url = '/login/'

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(
            user=self.request.user
        ).select_related('article', 'article__author')


class Detail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'ex00/detail.html'
    context_object_name = 'article'
    login_url = '/login/'


class Home(LoginRequiredMixin, RedirectView):
    pattern_name = 'ex00:articles'
    login_url = '/login/'


class Login(LoginView):
    template_name = 'ex00/login.html'

    def get_success_url(self):
        return reverse_lazy('ex00:home')
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    

class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('ex00:home')
    login_url = '/login/'

    
class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'ex00/register.html'
    success_url = reverse_lazy('ex00:login')


class Publish(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'synopsis', 'content']
    template_name = 'ex00/publish.html'
    success_url = reverse_lazy('ex00:publications')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class FavoriteToggle(LoginRequiredMixin, RedirectView):
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])

        favorite_query = UserFavouriteArticle.objects.filter(
            user=request.user, 
            article=article
        )

        if favorite_query.exists():
                favorite_query.delete()
        else:
            UserFavouriteArticle.objects.create(
                user=request.user, 
                article=article
            )
        return super().post(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        # Sends the user back to the page they were on
        return self.request.META.get('HTTP_REFERER', '/home/')