from django.shortcuts import render

from about.models import about_main, about_reward, about_author


def about_view(request):
    link_ru = '/ru/about/'
    link_en = '/en/about/'
    link_fr = '/fr/about/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'about_main': about_main.objects.first(),
    }

    return render(request, 'about.html', context=context)