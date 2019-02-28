from django.urls import path

from . import views

app_name = 'counterparties'

urlpatterns = [
    path('', views.index, name='index'),
]
