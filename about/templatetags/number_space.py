from django.template import Library

register = Library()

value = 9000


@register.filter()
def number_space(value):
    value = str(value)

    first = value[0]
    second = value[1:]
    my_value = first + ' ' + second

    return my_value
