from django import template

register = template.Library()

@register.filter
def extension(value):
    value = str(value)
    new_value = value[value.find(".") + 1:]
    return new_value
