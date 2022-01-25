from django.shortcuts import render
from .models import contact_main, contact_form


def contact_view(request):
    link_ru = '/ru/contacts/'
    link_en = '/en/contacts/'
    link_fr = '/fr/contacts/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'contact_main': contact_main.objects.first(),
        'contact_form': contact_form.objects.first()

    }

    return render(request, 'contacts.html', context=context)
