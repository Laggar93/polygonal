from django.shortcuts import render
from .models import index_main


def index_view(request):
    link_ru = '/ru/'
    link_en = '/en/'
    link_fr = '/fr/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'index_main': index_main.objects.first(),

    }

    return render(request, 'index.html', context=context)