from django.shortcuts import render


def index(request):
    return render(request, 'import/index.html')

def process(request):
    if request.method != 'POST' or 'csv' not in request.FILES:
        context = {'error': 'Geen bestand geüpload'}
        return render(request, 'import/index.html', context)
    file = request.FILES['csv']
    if file.content_type != 'text/csv':
        context = {'error': 'Geen geldig csv-bestand geüpload' }
        return render(request, 'import/index.html', context)
    return render(request, 'import/process.html')
