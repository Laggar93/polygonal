from django.shortcuts import render
from .models import contact_main
from shop.models import shop_page


def contact_view(request):
    link_ru = '/ru/contacts/'
    link_en = '/en/contacts/'
    link_fr = '/fr/contacts/'

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'contacts': contact_main.objects.all()

    }

    return render(request, 'contacts.html', context=context)
