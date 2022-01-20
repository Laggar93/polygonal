from django.shortcuts import render, get_object_or_404
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
        'advice_pages': advice_page.objects.all().order_by('order'),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,

    }

    return render(request, 'advice.html', context=context)


def advice_item_view(request, advice_page_slug):
    get_object_or_404(advice_page, slug=advice_page_slug, is_active=True)
    advice_pages = advice_page.objects.filter(slug=advice_page_slug, is_active=True).first()
    blocks = advice_blocks.objects.filter(advice_page=advice_pages).order_by('order')
    language = request.LANGUAGE_CODE

    if advice_page.objects.filter(slug=advice_page_slug, is_active_ru=True):
        link_ru = request.path.replace('/' + language + '/', '/ru/')
    else:
        link_ru = '/ru/advice/'

    if advice_page.objects.filter(slug=advice_page_slug, is_active_en=True):
        link_en = request.path.replace('/' + language + '/', '/en/')
    else:
        link_en = '/en/advice/'

    if advice_page.objects.filter(slug=advice_page_slug, is_active_fr=True):
        link_fr = request.path.replace('/' + language + '/', '/fr/')
    else:
        link_fr = '/fr/advice/'

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