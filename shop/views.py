from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, HttpResponse
from django.shortcuts import render

from .models import category, subcategory, item, shop_page, item_terms, item_photos, discount, item_basket
from .service import get_order_params


def update_basket(request):
    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()

    amount = 0
    for item_basket_object in item_basket.objects.filter(session_key=session_key):
        amount = amount + item_basket_object.amount

    if request.is_ajax() and request.GET:
        id = request.GET.get('id', None)
        # проверить, что id является числом и есть товар с таким айдишником, иначе ничего не делаем
        test = item_basket.objects.filter(session_key=session_key, item=item.objects.get(id=id)).first()
        if test:
            item_basket.objects.filter(session_key=session_key, item=item.objects.get(id=id)).delete()
        else:
            item_basket.objects.get_or_create(session_key=session_key, item=item.objects.get(id=id), amount=1)

    return amount, session_key


def update_basket_view(request):
    update_basket(request)
    return HttpResponse('')


def category_view(request, category_slug):
    language = request.LANGUAGE_CODE
    if language == 'en' or language == 'fr':
        if request.GET:
            currency = request.GET['currency']
            if currency != 'eur':
                currency = 'usd'
        else:
            currency = 'usd'
    else:
        currency = 'rub'

    query_param = request.GET.get('sort')
    get_object_or_404(category, slug=category_slug, is_active=True)
    active_category = category.objects.filter(slug=category_slug, is_active=True).first()

    if category.objects.filter(slug=category_slug, is_active_ru=True):
        link_ru = request.path.replace('/' + language + '/', '/ru/')
    else:
        link_ru = '/ru/shop/'

    if category.objects.filter(slug=category_slug, is_active_en=True):
        link_en = request.path.replace('/' + language + '/', '/en/')
    else:
        link_en = '/en/shop/'

    if category.objects.filter(slug=category_slug, is_active_fr=True):
        link_fr = request.path.replace('/' + language + '/', '/fr/')
    else:
        link_fr = '/fr/shop/'

    items = item.objects.filter(category__category=active_category).prefetch_related('category').order_by('name')

    if query_param:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(category__category=active_category).prefetch_related('category').order_by(param)

    categories = category.objects.all()
    subcategories = subcategory.objects.filter(category=active_category, is_active=True)

    discounts = discount.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'items': items,
        'active_category': active_category,
        'shop_page': shop_page.objects.first(),
        'query_param': query_param,
        'currency': currency,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'show_currency': True,
        'show_language': True,
        'discounts': discounts,
        'amount': update_basket(request)[0],
        'item_basket': item_basket.objects.filter(session_key=update_basket(request)[1]),
    }

    return render(request, 'catalog.html', context=context)


def first_category_for_url(request):
    active_category = category.objects.filter(is_active=True).first()
    path = active_category.slug

    return redirect(category_view, category_slug=path)


def subcategory_view(request, category_slug, subcategory_slug):
    language = request.LANGUAGE_CODE

    if language == 'en' or language == 'fr':
        if request.GET:
            currency = request.GET['currency']
            if currency != 'eur':
                currency = 'usd'
        else:
            currency = 'usd'
    else:
        currency = 'rub'

    query_param = request.GET.get('sort')
    active_category = category.objects.filter(slug=category_slug, is_active=True).first()
    active_subcategory = subcategory.objects.filter(slug=subcategory_slug, category=active_category, is_active=True).first()
    get_object_or_404(subcategory, slug=subcategory_slug, category=active_category, is_active=True)

    if subcategory.objects.filter(category=active_category, is_active_ru=True):
        link_ru = request.path.replace('/' + language + '/', '/ru/')
    else:
        link_ru = '/ru/shop/'

    if subcategory.objects.filter(category=active_category, is_active_en=True):
        link_en = request.path.replace('/' + language + '/', '/en/')
    else:
        link_en = '/en/shop/'

    if subcategory.objects.filter(category=active_category, is_active_fr=True):
        link_fr = request.path.replace('/' + language + '/', '/fr/')
    else:
        link_fr = '/fr/shop/'

    items = item.objects.filter(category=active_subcategory).order_by('name')

    if query_param:
        param = get_order_params(query_param)
        if param:
            items = item.objects.filter(category=active_subcategory).order_by(param)

    categories = category.objects.filter(is_active=True)
    subcategories = subcategory.objects.filter(category=active_category, is_active=True)

    discounts = discount.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'items': items,
        'discounts': discounts,
        'active_category': active_category,
        'active_subcategory': active_subcategory,
        'shop_page': shop_page.objects.first(),
        'query_param': query_param,
        'currency': currency,
        'show_currency': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'show_language': True,
    }

    return render(request, 'catalog.html', context=context)


def catalog_item(request, category_slug, subcategory_slug, item_slug):
    language = request.LANGUAGE_CODE
    if language == 'en' or language == 'fr':
        if request.GET:
            currency = request.GET['currency']
            if currency != 'eur':
                currency = 'usd'
        else:
            currency = 'usd'
    else:
        currency = 'rub'

    active_category = category.objects.filter(slug=category_slug, is_active=True).first()
    active_subcategory = subcategory.objects.filter(slug=subcategory_slug, category=active_category, is_active=True).first()
    get_object_or_404(item, slug=item_slug, category=active_subcategory, is_active=True)
    items = item.objects.filter(slug=item_slug, category=active_subcategory, is_active=True).first()
    item.objects.filter(slug=item_slug, category=active_subcategory, is_active=True).update(views=F("views") + 1)

    if item.objects.filter(slug=item_slug, category=active_subcategory, is_active_ru=True):
        link_ru = request.path.replace('/' + language + '/', '/ru/')
    else:
        link_ru = '/ru/shop/'

    if item.objects.filter(slug=item_slug, category=active_subcategory, is_active_en=True):
        link_en = request.path.replace('/' + language + '/', '/en/')
    else:
        link_en = '/en/shop/'

    if item.objects.filter(slug=item_slug, category=active_subcategory, is_active_fr=True):
        link_fr = request.path.replace('/' + language + '/', '/fr/')
    else:
        link_fr = '/fr/shop/'

    delivery_info = item_terms.objects.filter(item=items)
    related_items = item.objects.filter(category__category=active_category).exclude(slug=item_slug)[:6]
    related_categories = items.connected_items.all()
    items_photos = item_photos.objects.filter(item=items)
    item_discounts = discount.objects.filter(item=items).first()
    if item_discounts:
        output_discount = item_discounts.get_currency_price()
    else:
        output_discount = None

    context = {
        'items': items,
        'discount': output_discount,
        'active_category': active_category,
        'active_subcategory': active_subcategory,
        'shop_page': shop_page.objects.first(),
        'related_items': related_items,
        'related_categories': related_categories,
        'delivery_info': delivery_info,
        'items_photos': items_photos,
        'item_discounts': item_discounts,
        'currency': currency,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'show_currency': True,
        'show_language': True,
    }
    return render(request, 'catalog_item.html', context=context)


def order_view(request):
    
    language = request.LANGUAGE_CODE
    
    if language == 'en' or language == 'fr':
        if request.GET:
            currency = request.GET['currency']
            if currency != 'eur':
                currency = 'usd'
        else:
            currency = 'usd'
    else:
        currency = 'rub'
    link_en = '/en/cart/'
    link_fr = '/fr/cart'
    link_ru = '/ru/cart/'
    
    session_key = request.session.session_key
    
    if not session_key:
        request.session.cycle_key()
    
    if request.GET:
    #if request.is_ajax() and request.GET:
        id = request.GET.get('id', None)
        # проверить, что id является числом и есть товар с таким айдишником, иначе ничего не делаем
        action = request.GET.get('action', None)
        # проверить, что action принял значение add или minus или remove
        test = item_basket.objects.filter(session_key=session_key, item=item.objects.filter(id=id).first())
        if test:
            if action == 'add':
                # берем текущий amount
                # увеличить amount на 1
                # делаем апдейт
                print('plus')
            if action == 'minus':
                # берем текущий amount
                # если amount = 1, то товар удаляется
                # если больше 1, то уменьшить amount на 1
                # делаем апдейт
                print('minus')
            if action == 'remove':
                # удаляем текущий товар
                print('remove')
    
    item_basket_amount = 0
    
    for i in item_basket.objects.filter(session_key=session_key):
        item_basket_amount = item_basket_amount + i.amount

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'item_basket': item_basket.objects.filter(session_key=session_key),
        'item_basket_amount': item_basket_amount,
        'shop_page': shop_page.objects.first(),
        'currency': currency,
        'show_currency': True,
    }
    return render(request, 'cart.html', context=context)


def handler404(request, exception):
    shop_pages = shop_page.objects.all().first()
    context = {
        'shop_page': shop_page.objects.first(),

    }
    return render(request, '404.html', status=404, context=context)
