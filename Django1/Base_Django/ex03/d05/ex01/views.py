from django.shortcuts import render


# Create your views here.
def django_intro(request):
    return render(request, "ex01/django.html", context={})


def display_processes(request):
    return render(request, "ex01/display.html", context={})


def template_engine(request):
    return render(request, "ex01/templates.html", context={})
