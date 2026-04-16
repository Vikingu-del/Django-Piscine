from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from d06.data import movies as movie_data
from .forms import MovieForm


def populate(request):
    results = []
    for data in movie_data:
        try:
            movie = Movies.objects.create(**data)
            results.append(f"OK - {movie} added to the database")
        except Exception as e:
            results.append(f"Error - {str(e)}")
    return render(request, 'ex07/populate.html', {'results': results})


def display(request):
    movies = Movies.objects.all().order_by('episode_nb')
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex07/display.html', {'movies': movies})
    

def update(request):
    movies = Movies.objects.all().order_by('episode_nb')
    if not movies:
        return HttpResponse("No data available")
    movie_choices = [(m.title, m.title) for m in movies]

    if request.method == 'POST':
        form = MovieForm(request.POST, choices=movie_choices)
        if form.is_valid():
            selected_titles = form.cleaned_data['titles']
            new_opening_crawl = form.cleaned_data['opening_crawl']
            try:
                movie = Movies.objects.get(title=selected_titles)
                movie.opening_crawl = new_opening_crawl
                # We can aslo say movie.update(opening_crawl = new_opening_crawl)
                # But it will bypass the auto feature
                movie.save()
                return redirect('ex07:update')
            except Exception:
                return HttpResponse("No data available")
            
    else:
        form = MovieForm(choices=movie_choices)
    return render(request, 'ex07/form.html', {'form': form})