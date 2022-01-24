from advice.models import advice_main
from delivery.models import delivery_main
from shop.models import item
from order_projects.models import project_page


def globals(request):
    context = {
        'items': item.objects.all(),
        ''
        'project_pages': project_page.objects.first(),
        'advice_main': advice_main.objects.first(),
        'delivery_mains': delivery_main.objects.first(),
    }
    return context