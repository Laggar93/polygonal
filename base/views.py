from django.shortcuts import render
from base.models import rules, offer, policy


def rules_view(request):
    link_ru = '/ru/rules/'
    link_en = '/en/rules/'
    link_fr = '/fr/rules/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'rules': rules.objects.first()
    }

    return render(request, 'rules.html', context=context)


def offer_view(request):
    link_ru = '/ru/offer/'
    link_en = '/en/offer/'
    link_fr = '/fr/offer/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'offer': offer.objects.first()
    }

    return render(request, 'offer.html', context=context)


def policy_view(request):
    link_ru = '/ru/policy/'
    link_en = '/en/policy/'
    link_fr = '/fr/policy/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'policy': policy.objects.first()
    }

    return render(request, 'policy.html', context=context)