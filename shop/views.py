from django.db.models.fields import related
from django.shortcuts import get_object_or_404, redirect
from .models import category, subcategory, item, shop_page, item_terms
from django.shortcuts import render
from .service import get_order_params


def category_view(request, category_slug):
    query_param = request.GET.get('sort')
    get_object_or_404(category, slug=category_slug)

    items = item.objects.filter(
        category__category__slug=category_slug).prefetch_related(
        'category').order_by('name')

    if query_param:
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
        'shop_page': shop_page.objects.first(),
        'query_param': query_param,
    }

    return render(request, 'catalog.html', context=context)


def first_category_for_url(request):
    active_category = category.objects.all().first()
    path = active_category.slug

    return redirect(category_view, category_slug=path)


def subcategory_view(request, category_slug, subcategory_slug):
    query_param = request.GET.get('sort')
    get_object_or_404(category, slug=category_slug)
    get_object_or_404(subcategory, slug=subcategory_slug,
                      category=category.objects.filter(
                          slug=category_slug).first())

    items = item.objects.filter(category__category__slug=category_slug,
                                category__slug=subcategory_slug).order_by(
        'name')

    if query_param:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(
                category__category__slug=category_slug,
                category__slug__in=subcategory_slug).order_by(
                param)

    categories = category.objects.all()
    subcategories = subcategory.objects.filter(category__slug=category_slug)
    active_category = category.objects.filter(slug=category_slug).first()
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'items': items,
        'active_category': active_category,
        'shop_page': shop_page.objects.first(),
        'query_param': query_param,
    }

    return render(request, 'catalog.html', context=context)


def catalog_item(request, category_slug, subcategory_slug, item_slug):
    get_object_or_404(category, slug=category_slug)
    get_object_or_404(subcategory, slug=subcategory_slug,
                      category=category.objects.filter(
                          slug=category_slug).first())
    get_object_or_404(item, slug=item_slug)
    items = item.objects.filter(slug=item_slug).first()
    delivery_info = item_terms.objects.filter(item__slug=item_slug)
    related_items = item.objects.filter(category__slug=subcategory_slug).exclude(slug=item_slug)[:6]
    related_categories = items.connected_items.all()
    context = {
        'items': items,
        'shop_page': shop_page.objects.first(),
        'related_items': related_items,
        'related_categories': related_categories,
        'delivery_info': delivery_info,
    }
    return render(request, 'catalog_item.html', context=context)


def handler404(request, exception):
    return render(request, '404.html', status=404)
