from django.shortcuts import render
from shop.models import shop_page


def about_view(request):
    link_ru = '/ru/about/'
    link_en = '/en/about/'
    link_fr = '/fr/about/'

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
    }

    return render(request, 'about.html', context=context)