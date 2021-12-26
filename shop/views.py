from django.shortcuts import get_object_or_404
from .models import Category, SubCategory, item
from django.shortcuts import render
from .service import get_order_params


def item_view(request, category_slug, subcategory_slug, item_slug):
    subcategory_item = SubCategory.objects.filter(slug=subcategory_slug).first()
    get_object_or_404(item, slug=item_slug, category=subcategory_item)
    content = {
        'category_slug': category_slug,
        'subcategory_slug': subcategory_slug,
        'item_slug': item_slug
    }
    return render(request, 'catalog-item.html', content)


def order_view(request):
    pass


def category_view(request, category_slug, *args, **kwargs):
    query_param = request.GET.get('sort')
    is_category = Category.objects.filter(slug=category_slug).exists()
    if is_category:
        items = item.objects.filter(
            category__category__slug=category_slug).prefetch_related(
            'category').order_by('name')
        if query_param and query_param != None:
            param = get_order_params(query_param)
            if param:
                items = item.objects.filter(
                    category__category__slug=category_slug).prefetch_related(
                    'category').order_by(param)

        categories = Category.objects.all()
        subcategories = SubCategory.objects.filter(category__slug=category_slug)
        active_category = Category.objects.filter(slug=category_slug).first()

        context = {
            'categories': categories,
            'subcategories': subcategories,
            'items': items,
            'active_category': active_category
        }

        return render(request, 'catalog.html', context=context)
    return render(request, '404.html')


def subcategory_view(request, category_slug, subcategory_slug):
    query_param = request.GET.get('sort')
    is_instance = Category.objects.filter(
        in_category__slug=subcategory_slug).exists()
    if is_instance:
        items = item.objects.filter(category__category__slug=category_slug,
                                    category__slug=subcategory_slug).order_by(
            'name')
        if query_param:
            param = get_order_params(query_param)
            if param:
                items = item.objects.filter(
                    category__category__slug=category_slug,
                    category__slug=subcategory_slug).order_by(
                    param)

        category = Category.objects.all()
        subcategory = SubCategory.objects.filter(category__slug=category_slug)

        active_category = Category.objects.filter(slug=category_slug).first()

        context = {
            'categories': category,
            'subcategories': subcategory,
            'items': items,
            'active_category': active_category
        }

        return render(request, 'catalog.html', context=context)

    return render(request, '404.html')
