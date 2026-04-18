from django.shortcuts import render
from django.http import HttpResponse
from .models import Planets, People

# Create your views here.
def display(request):
    peoples = People.objects.select_related(
        'homeworld'
    ).filter(
        homeworld__climate__icontains='windy' # lookup syntax
    ).order_by('name')
    if not People.objects.exists():
        error_msg = (
            "No data available, please use the following command line before use: "
            "python3 manage.py loaddata ex09_initial_data.json"
        )
        return HttpResponse(error_msg)

    return render(request, 'ex09/display.html', {'peoples': peoples})