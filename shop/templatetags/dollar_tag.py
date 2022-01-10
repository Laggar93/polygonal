from django.template import Library
register = Library()


@register.filter()
def dollar_tag(value):
    value_dec = str(value - int(value))[1:]
    if value_dec == '.0':
        value = int(value)
    else:
        value = value

    return value
