from django.shortcuts import render
from .models import project_page, project_images, project_list
from shop.models import shop_page


def projects_view(request):

    link_ru = '/ru/projects/'
    link_en = '/en/projects/'
    link_fr = '/fr/projects/'


    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'project_pages': project_page.objects.first(),
        'project_lists': project_list.objects.all(),

    }

    return render(request, 'projects.html', context=context)