from django.shortcuts import render
from .models import *
from shop.models import shop_page


def advice_view(request):

    link_ru = '/ru/advice/'
    link_en = '/en/advice/'
    link_fr = '/fr/advice/'
    # print(advice_page.main_photo_xxl)
    # advice_pages = advice_page.objects.all().first()

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'advice_main': advice_main.objects.first(),
        'advice_pages': advice_page.objects.all(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,

    }

    return render(request, 'advice.html', context=context)


def advice_item_view(request, advice_page_slug):

    link_ru = '/ru/advice/'
    link_en = '/en/advice/'
    link_fr = '/fr/advice/'
    advice_pages = advice_page.objects.filter(slug=advice_page_slug, is_active=True).first()
    blocks = advice_blocks.objects.get(advice_page__slug=advice_page_slug)

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'advice_main': advice_main.objects.first(),
        'advice_pages': advice_pages,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'blocks': blocks,

    }


    return render(request, 'advice-item.html', context=context)