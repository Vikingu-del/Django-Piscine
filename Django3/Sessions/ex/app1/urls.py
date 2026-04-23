from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('vote/<int:tip_id>/<str:action>/', views.vote, name='vote'),
    path('delete/<int:tip_id>/', views.delete, name='delete'),
]
