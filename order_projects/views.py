from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import project_page, project_images, project_list
from shop.models import shop_page


def projects_view(request):
    get_object_or_404(project_page)
    # projects = project_page.objects.all()
    link_ru = '/ru/projects/'
    link_en = '/en/projects/'
    link_fr = '/fr/projects/'
    project_items = project_page.objects.all()
    project_lists = project_list.objects.all()

    context = {
        'show_language': True,
        'shop_page': shop_page.objects.first(),
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'project_items': project_items,
        'project_lists': project_lists,

    }

    return render(request, 'projects.html', context=context)