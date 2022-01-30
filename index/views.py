from django.shortcuts import render

from about.models import about_main
from order_projects.models import project_page
from shop.models import category, shop_page
from .models import index_main, order_point, index_translate


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
        'categories': category.objects.all(),
        'project_page': project_page.objects.first(),
        'points': order_point.objects.all(),
        'about_main': about_main.objects.first(),
        'shop_page': shop_page.objects.first(),
        'index_translate': index_translate.objects.first(),

    }

    return render(request, 'index.html', context=context)