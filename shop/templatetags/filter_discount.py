from django.utils import timezone
from django import template

register = template.Library()

@register.filter
def filter_discount(discount, items):
    item_discounts = discount.filter(item=items).first()
    if item_discounts:
        output_discount = item_discounts.get_currency_price()
    else:
        output_discount = None
    return output_discount