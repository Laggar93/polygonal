from django.template import Library
register = Library()


@register.filter()
def price_space(value):
    if isinstance(value, float):

        value = int(value)
        my_value = [i for i in str(value)]
        my_value.insert(1, ' ')
        my_value = ''.join(my_value)


        return my_value


