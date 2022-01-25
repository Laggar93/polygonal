from about.models import about_main
from advice.models import advice_main
from contact.models import contact_main
from delivery.models import delivery_main
from map.models import map_main
from shop.models import item, shop_page
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
    }
    return context