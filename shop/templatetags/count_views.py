from django import template

register = template.Library()

@register.filter
def count_views(item, views):
    print(item)
    #item.update(views=views+1)
