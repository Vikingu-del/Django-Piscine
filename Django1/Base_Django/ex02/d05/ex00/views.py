from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = loader.get_template("ex00/index.html")
    return HttpResponse(template.render({}, request))
