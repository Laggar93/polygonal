from django.shortcuts import render
from .models import *
from shop.models import shop_page


def delivery_main_view(request):
    link_ru = '/ru/delivery/'
    link_en = '/en/delivery/'
    link_fr = '/fr/delivery/'

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'delivery_main': delivery_main.objects.first(),
        'delivery_articles': delivery_article.objects.all().order_by('order')

    }

    return render(request, 'delivery.html', context=context)



