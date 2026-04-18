from django.shortcuts import render
from django.http import HttpResponse
from d06.utils import load_query, get_sql_path, execute_query, copy_from_csv_to_db


# Create your views here.
def init(request):
    query = load_query(get_sql_path('ex08', 'schema.sql'))
    try:
        execute_query(query, type='commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def populate(request):
    configs = {
        'ex08_planets': (
            ('name', 'climate', 'diameter', 'orbital_period',
             'population', 'rotation_period', 'surface_water', 'terrain'), 
            'planets.csv'
        ),
        'ex08_people': (
            ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 
             'height', 'mass', 'homeworld'), 
            'people.csv'
        )
    }
    results = copy_from_csv_to_db('ex08', configs)
    return render(request, 'ex08/populate.html', {'results': results})


def display(request):
    query = load_query(get_sql_path('ex08', 'fetch.sql'))
    try:
        data = execute_query(query, type='fetch')
        return render(request, 'ex08/display.html', {'peoples': data})
    except Exception:
        return HttpResponse("No data available")
