from django.shortcuts import render
from .models import *
from shop.models import shop_page
from delivery.models import delivery_main


def contact_view(request):
    link_ru = '/ru/contact/'
    link_en = '/en/contact/'
    link_fr = '/fr/contact/'

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),

        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,

    }

    return render(request, 'contacts.html', context=context)
