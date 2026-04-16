from django.shortcuts import render
from django.http import HttpResponse
from d06.utils import load_query, get_sql_path, execute_query

# Create your views here.
def init(request):
    query = load_query(get_sql_path('ex08', 'schema.sql'))
    try:
        execute_query(query, type='commit')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))

