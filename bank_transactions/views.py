from django.shortcuts import render


def index(request):
    return render(request, 'bank_transactions/index.html')
