from django.urls import path

from . import views

app_name = 'bank_transactions'

urlpatterns = [
    path('process', views.process, name='process'),
    path('', views.index, name='index'),
]
