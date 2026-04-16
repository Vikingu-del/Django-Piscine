from django.shortcuts import render
from .models import Movies
from d06.data import movies as movie_data


# Create your views here.
def populate(request):
    results = []
    for data in movie_data:
        try:
            movie = Movies.objects.create(**data)
            results.append(f"OK - {movie} added to database")
        except Exception as e:
            results.append(f"Error - {str(e)}")
    return render(request, 'ex03/populate.html', {'results': results})

def display(request):
    movies = Movies.objects.all().order_by('episode_nb')
    if not movies:
        return render(request, 'ex03/display.html', {'movies': None})
    return render(request, 'ex03/display.html', {'movies': movies})