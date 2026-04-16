from django.urls import path
from .views import init, populate, display, update

app_name = 'ex06'

urlpatterns = [
    path('init/', init, name='init'),
    path('populate/', populate, name='populate'),
    path('display/', display, name='display'),
    path('update/', update, name='update'),
]
