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
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,

    }

    return render(request, 'advice.html', context=context)


def advice_item_view(request):

    link_ru = '/ru/advice_item/'
    link_en = '/en/advice_item/'
    link_fr = '/fr/advice_item/'

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'advice_main': advice_main.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,

    }

    return render(request, 'advice-item.html', context=context)