from django.shortcuts import render

from map.models import map_main, map_town


def map_view(request):
    link_ru = '/ru/map/'
    link_en = '/en/'
    link_fr = '/fr/'


    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'map_main': map_main.objects.first(),
        'map_town': map_town.objects.all()

    }

    return render(request, 'map.html', context=context)
