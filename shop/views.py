from django.db.models.fields import related
from django.shortcuts import get_object_or_404, redirect
from .models import category, subcategory, item, shop_page, item_terms, \
    item_photos
from django.shortcuts import render
from django.db.models import F
from .service import get_order_params


def category_view(request, category_slug):
    query_param = request.GET.get('sort')
    get_object_or_404(category, slug=category_slug)
    active_category = category.objects.filter(slug=category_slug).first()

    items = item.objects.filter(
        category__category=active_category).prefetch_related(
        'category').order_by('name')

    if query_param:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(
                category__category=active_category).prefetch_related(
                'category').order_by(param)

    categories = category.objects.all()
    subcategories = subcategory.objects.filter(category=active_category)

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
    active_category = category.objects.filter(slug=category_slug).first()
    active_subcategory = subcategory.objects.filter(slug=subcategory_slug,
                                                    category=active_category).first()

    get_object_or_404(subcategory, slug=subcategory_slug,
                      category=active_category)

    items = item.objects.filter(category=active_subcategory).order_by(
        'name')

    if query_param:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(
                category=active_subcategory).order_by(
                param)

    categories = category.objects.all()
    subcategories = subcategory.objects.filter(category=active_category)

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
    active_category = category.objects.filter(slug=category_slug).first()
    active_subcategory = subcategory.objects.filter(slug=subcategory_slug,
                                                    category=active_category).first()
    get_object_or_404(item, slug=item_slug,
                      category=active_subcategory)
    items = item.objects.filter(slug=item_slug).first()

    # counter = item.objects.filter(slug=item_slug).update(views=F("views") + 1)
    # counter = item.objects.filter(slug=item_slug).first()


    # counter = 0
    # counter.views = F('views') + 1
    # counter.save()


    # counter = item.objects.get(views=item.views)
    # counter.views = F("views") + 1
    # counter.save()


    counter = item.objects.filter(slug=item_slug, category=active_subcategory)
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter+1


    delivery_info = item_terms.objects.filter(item=items)
    related_items = item.objects.filter(
        category__slug=subcategory_slug).exclude(slug=item_slug)[:6]
    related_categories = items.connected_items.all()
    items_photos = item_photos.objects.filter(item=items)
    context = {
        'items': items,
        'counter': counter,
        'active_category': active_category,
        'active_subcategory': active_subcategory,
        'shop_page': shop_page.objects.first(),
        'related_items': related_items,
        'related_categories': related_categories,
        'delivery_info': delivery_info,
        'items_photos': items_photos,
    }
    return render(request, 'catalog_item.html', context=context)


def handler404(request, exception):
    shop_pages = shop_page.objects.all().first()
    context = {
        'shop_pages': shop_pages
    }
    return render(request, '404.html', status=404, context=context)
