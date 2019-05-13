from django.urls import path

from . import views

app_name = 'bank_transactions'

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('contra_accounts/unlinked', views.unlinked_contra_accounts, name='unlinked_contra_accounts'),
]
