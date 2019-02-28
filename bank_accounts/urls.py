from django.urls import path

from . import views

app_name = 'bank_accounts'

urlpatterns = [
    path('', views.index, name='index'),
]
