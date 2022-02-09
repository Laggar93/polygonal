from django.template import Library
register = Library()


@register.filter()
def euro_tag(value):
    if value:
        value_dec = str(value - int(value))[1:]
        if value_dec == '.0':
            value = int(value)
        elif value_dec != '.0':
            value = round(value, 1)
        else:
            value = value

        return value