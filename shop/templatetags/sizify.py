from django import template

register = template.Library()

def sizify(value, translate):

    return str(round(value / 1048576, 2)).replace(',', '.') + ' ' + translate


register.filter('sizify', sizify)