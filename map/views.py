from django.shortcuts import render

from map.models import map_main
from shop.models import shop_page


def map_view(request):
    link_ru = '/ru/map/'
    link_en = '/en/shop/'
    link_fr = '/fr/shop/'


    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,

    }

    return render(request, 'map.html', context=context)
