from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def convert_length(request):
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        conversion_factors = {
            'km': 1_000,
            'm': 1,
            'dm': 0.1,
            'cm': 0.01,
            'mm': 0.001
        }

        result = value * conversion_factors[from_unit] / conversion_factors[to_unit]
        return render(request, 'index.html', {'length_result': result})


def convert_weight(request):
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        conversion_factors = {
            'ton': 1_000_000,
            'sr': 100_000,
            'kg': 1_000,
            'gr': 1
        }

        result = value * conversion_factors[from_unit] / conversion_factors[to_unit]
        return render(request, 'index.html', {'weight_result': result})
