from django import template

register = template.Library()

@register.filter(name='split_by_hash')
def split_by_hash(value):
    return value.split("#")

# custom filter to get an item from the dictionary used in navbar
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)