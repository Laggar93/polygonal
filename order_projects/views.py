from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import project_page, project_images, project_list


def projects_view(request):
    # get_object_or_404(project_page)
    # projects = project_page.objects.all()

    context = {
    }

    return render(request, 'projects.html', context=context)