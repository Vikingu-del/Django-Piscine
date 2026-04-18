from django.shortcuts import render
from django.http import HttpResponse
from .models import Planets, People, Movies
from .forms import SearchForm

# Create your views here.
def index(request):
    results = None
    form = SearchForm(request.GET or None)

    if request.GET and form.is_valid():
        data = form.cleaned_data
        results = Movies.objects.filter(
            release_date__gte=data['min_release_date'],
            release_date__lte=data['max_release_date'],
            characters__gender=data['gender'],
            characters__homeworld__diameter__gte=data['min_diameter']
        ).values(
            'title', 
            'characters__name', 
            'characters__gender', 
            'characters__homeworld__name', 
            'characters__homeworld__diameter'
        )

    return render(request, 'ex10/form.html', {
        'form': form,
        'results': results,
    })
