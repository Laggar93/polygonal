from shop.models import item


def globals(request):
    context = {
        'items': item.objects.all(),
    }
    return context