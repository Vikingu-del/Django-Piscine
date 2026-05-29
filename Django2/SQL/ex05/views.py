from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from d06.data import movies as movie_data
from .forms import MovieForm


# Create your views here.
def populate(request):
    results = []
    for data in movie_data:
        try:
            movie = Movies.objects.create(**data)
            results.append(f"OK - {movie} added to database")
        except Exception as e:
            results.append(f"Error - {str(e)}")
    return render(request, "ex05/populate.html", {"results": results})


def display(request):
    movies = Movies.objects.all().order_by("episode_nb")
    if not movies:
        return render(request, "ex05/display.html", {"movies": None})
    return render(request, "ex05/display.html", {"movies": movies})


def remove(request):
    movies = Movies.objects.all().order_by("episode_nb")
    if not movies:
        return HttpResponse("No data available")
    movie_choices = [(m.title, m.title) for m in movies]
    if request.method == "POST":
        form = MovieForm(request.POST, choices=movie_choices)
        if form.is_valid():
            selected_title = form.cleaned_data["titles"]
            try:
                Movies.objects.get(title=selected_title).delete()
                return redirect("ex05:remove")
            except Exception as e:
                return HttpResponse(str(e))
    else:
        form = MovieForm(choices=movie_choices)
    return render(request, "ex05/form.html", {"form": form})
