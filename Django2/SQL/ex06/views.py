from django.shortcuts import render, redirect
from django.http import HttpResponse
from d06.utils import load_query, get_sql_path, execute_query
from d06.data import movies as movie_data
from .forms import MovieForm


# Create your views here.
def init(request):
    query = load_query(get_sql_path('ex06', 'schema.sql'))
    try:
        execute_query(query, type='commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def populate(request):
    results = []
    for data in movie_data:
        query = f"""
        INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date) VALUES
        ({data['episode_nb']}, '{data['title']}', '{data['director']}', '{data['producer']}', '{data['release_date']}')
        """
        try:
            execute_query(query, type='commit')
            results.append(f"OK - {data['title']} added to database")
        except Exception as e:
            results.append(f"Error - {str(e)}")
    return render(request, 'ex06/populate.html', {'results': results})


def display(request):
    query = load_query(get_sql_path('ex06', 'fetch.sql'))
    try:
        data = execute_query(query, type='fetch')
        return render(request, 'ex06/display.html', {'movies': data})
    except Exception as e:
        return HttpResponse(str(e))
    

def update(request):
    try:
        query = "SELECT title FROM ex06_movies;"
        data = execute_query(query, type='fetch')
        if not data:
            return HttpResponse("No data available")
        movie_choices = [(m['title'], m['title']) for m in data]
    except Exception:
        return HttpResponse("No data available")

    if request.method == 'POST':
        form = MovieForm(request.POST, choices=movie_choices)
        if form.is_valid():
            selected_titles = form.cleaned_data['titles']
            new_opening_crawl = form.cleaned_data['opening_crawl']
            update_query = f"UPDATE ex06_movies SET opening_crawl='{new_opening_crawl}' WHERE title='{selected_titles}';"
            try:
                execute_query(update_query, params=(new_opening_crawl, selected_titles), type='commit')
                return redirect('ex06:update')
            except Exception:
                return HttpResponse("No data available")
            
    else:
        form = MovieForm(choices=movie_choices)
    return render(request, 'ex06/form.html', {'form': form})