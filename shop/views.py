from django.shortcuts import get_object_or_404, redirect
from .models import category, subcategory, item
from django.shortcuts import render
from .service import get_order_params


def category_view(request, category_slug):
    query_param = request.GET.get('sort')
    get_object_or_404(category, slug=category_slug)

    items = item.objects.filter(
        category__category__slug=category_slug).prefetch_related(
        'category').order_by('name')

    if not items:
        categories = category.objects.all()
        subcategories = subcategory.objects.filter(category__slug=category_slug)
        active_category = category.objects.filter(slug=category_slug).first()
        context = {
            'categories': categories,
            'subcategories': subcategories,
            'active_category': active_category
        }
        return render(request, 'no_items.html', context=context)

    if query_param and query_param != None:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(
                category__category__slug=category_slug).prefetch_related(
                'category').order_by(param)

    categories = category.objects.all()
    subcategories = subcategory.objects.filter(category__slug=category_slug)
    active_category = category.objects.filter(slug=category_slug).first()

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'items': items,
        'active_category': active_category,
    }

    return render(request, 'catalog.html', context=context)


def first_category_for_url(request):
    active_category = category.objects.all().first()
    path = active_category.slug

    return redirect(category_view, category_slug=path)


def subcategory_view(request, category_slug, subcategory_slug):
    query_param = request.GET.get('sort')
    subcategory_slug = subcategory_slug.split(' ')
    get_object_or_404(category, slug=category_slug)
    get_object_or_404(subcategory, slug=subcategory_slug[0],
                      category=category.objects.filter(
                          slug=category_slug).first())

    items = item.objects.filter(category__category__slug=category_slug,
                                category__slug=subcategory_slug[0]).order_by(
        'name')

    if not items:
        categories = category.objects.all()
        subcategories = subcategory.objects.filter(category__slug=category_slug)
        active_category = category.objects.filter(slug=category_slug).first()
        context = {
            'categories': categories,
            'subcategories': subcategories,
            'active_category': active_category
        }
        return render(request, 'no_items.html', context=context)

    if query_param:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(
                category__category__slug=category_slug,
                category__slug=subcategory_slug).order_by(
                param)

    categories = category.objects.all()
    subcategories = subcategory.objects.filter(category__slug=category_slug)
    active_category = category.objects.filter(slug=category_slug).first()

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'items': items,
        'active_category': active_category,

    }

    return render(request, 'catalog.html', context=context)


def catalog_item(request, category_slug, subcategory_slug, item_slug):
    items = item.objects.filter(slug=item_slug)
    context = {
        'items': items
    }
    return render(request, 'catalog-item.html', context=context)


def handler404(request, exception):
    return render(request, '404.html', status=404)
