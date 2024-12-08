from django import template

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """Split a string into a list using the delimiter"""
    if value:
        return [x.strip() for x in value.split(delimiter)]
    return [] 