from django.urls import path

from . import views

app_name = 'import'

urlpatterns = [
    path('', views.index, name='index'),
]
