from about.models import about_main
from advice.models import advice_main
from base.models import footer_elements, rules, offer, policy
from contact.models import contact_main
from delivery.models import delivery_main
from map.models import map_main
from shop.models import item, shop_page, item_basket
from shop.views import update_basket
from order_projects.models import project_page


def globals(request):
    context = {
        'items': item.objects.all(),
        'shop_page': shop_page.objects.first(),
        'project_pages': project_page.objects.first(),
        'advice_main': advice_main.objects.first(),
        'delivery_main': delivery_main.objects.first(),
        'contact_main': contact_main.objects.first(),
        'map_main': map_main.objects.first(),
        'about_main': about_main.objects.first(),
        'footer_elements': footer_elements.objects.first(),
        'rules': rules.objects.first(),
        'offer': offer.objects.first(),
        'policy': policy.objects.first(),
        'amount': update_basket(request)[0],
        'item_basket': item_basket.objects.filter(session_key=update_basket(request)[1]),
    }
    return context