# from unicodedata import category
from django import template


register = template.Library()


@register.filter
def snipet(value, arg=20):

    return value[0:arg] + "..."
