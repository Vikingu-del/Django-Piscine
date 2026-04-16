from django.shortcuts import render
from django.http import HttpResponse
from d06.utils import load_query, get_sql_path, execute_query
from d06.data import movies as movie_data

# Create your views here.
def init(request):
    query = load_query(get_sql_path('ex02', 'schema.sql'))
    try:
        execute_query(query, type='commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def populate(request):
    results = []
    for data in movie_data:
        query = f"""
        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) VALUES
        ({data['episode_nb']}, '{data['title']}', '{data['director']}', '{data['producer']}', '{data['release_date']}')
        """
        try:
            execute_query(query, type='commit')
            results.append(f"OK - {data['title']} added to database")
        except Exception as e:
            results.append(f"Error - {str(e)}")
    return render(request, 'ex02/populate.html', {'results': results})
    

def display(request):
    query = load_query(get_sql_path('ex02', 'fetch.sql'))
    try:
        data = execute_query(query, type='fetch')
        return render(request, 'ex02/display.html', {'movies': data})
    except Exception as e:
        return HttpResponse(str(e))
