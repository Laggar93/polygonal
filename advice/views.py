from django.shortcuts import render
from .models import *
from shop.models import shop_page


def advice_view(request):

    link_ru = '/ru/advice/'
    link_en = '/en/advice/'
    link_fr = '/fr/advice/'

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

    # нет проверки 404

    # сделать проверку на наличие совета в других языках и вывести верную ссылку

    link_ru = '/ru/advice/'
    link_en = '/en/advice/'
    link_fr = '/fr/advice/'
    
    advice_pages = advice_page.objects.filter(slug=advice_page_slug, is_active=True).first()
    blocks = advice_blocks.objects.filter(advice_page=advice_pages)

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