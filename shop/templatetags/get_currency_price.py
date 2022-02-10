from django.utils import timezone
from django import template

register = template.Library()

@register.filter
def get_currency_price(value, currency):
        item = value.item.first()
        right_now = timezone.now().date()
        if value.starts <= right_now <= value.ends:
            results = [None, None, None]
            if value.type == '2':
                if item.price_rub:
                    item.price_rub = item.price_rub - value.amount_ru
                    results[0] = item.price_rub
                if item.price_usd:
                    item.price_usd = item.price_usd - value.amount_usd
                    results[1] = item.price_usd
                if item.price_eur:
                    item.price_eur = item.price_eur - value.amount_eur
                    results[2] = item.price_eur
                return results[currency]
            if value.type == '1':
                if item.price_rub:
                    item.price_rub = item.price_rub - ((item.price_rub / 100) * value.amount_ru)
                    results[0] = item.price_rub
                if item.price_usd:
                    item.price_usd = item.price_usd - ((item.price_usd / 100) * value.amount_usd)
                    results[1] = item.price_usd
                if item.price_eur:
                    item.price_eur = item.price_eur - ((item.price_eur / 100) * value.amount_eur)
                    results[2] = item.price_eur
                return results[currency]
        else:
            if item.price_rub:
                item.price_rub = item.price_rub
            if item.price_usd:
                item.price_usd = item.price_usd
            if item.price_eur:
                item.price_eur = item.price_eur