from django.http import HttpResponse
from django.shortcuts import render

from .utils import INGBankStatementParser


def index(request):
    return render(request, 'bank_transactions/index.html')

def process(request):
    if request.method != 'POST' or 'csv' not in request.FILES:
        context = {'error': 'Geen bestand geüpload'}
        return render(request, 'import/index.html', context)
    file = request.FILES['csv']
    if file.content_type != 'text/csv':
        context = {'error': 'Geen geldig csv-bestand geüpload'}
        return render(request, 'import/index.html', context)
    data = file.read().decode('utf-8')
    csvparser = INGBankStatementParser(data)
    if csvparser.is_clean():
        if csvparser.is_valid():
            contra_accounts = csvparser.handle_contra_accounts()
            #return render(request, 'bank_transactions/process.html', {'data': csvparser.rows})
            return render(request, 'bank_transactions/process.html', {'data': contra_accounts})
        else:
            return HttpResponse('<br />'.join(csvparser.validation_errors()))
    else:
        return HttpResponse('<br />'.join(csvparser.get_sanitisation_errors()))
