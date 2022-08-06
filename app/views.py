from collections import Counter
from django.http import HttpResponse

from django.shortcuts import render

counter_show = Counter()
counter_click = Counter()

def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    name = request.GET.get('from-landing')
    counter_click[name] += 1
    return render(request, 'index.html')

def landing(request):
    name = request.GET.get('ab-test-arg')
    counter_show[name] += 1
    if name == 'original':
        return render(request, 'landing.html')
    elif name == 'test':
        return render(request, 'landing_alternate.html')


def stats(request):
    try:
        TEST_CONVERSION = counter_click['test'] / counter_show['test']
        ORIGINAL_CONVERSION = counter_click['original'] / counter_show['original']
        return render(request, 'stats.html', context={
            'test_conversion': TEST_CONVERSION,
            'original_conversion': ORIGINAL_CONVERSION,
        })
    except:
        response = 'упс'
        return HttpResponse(response)


