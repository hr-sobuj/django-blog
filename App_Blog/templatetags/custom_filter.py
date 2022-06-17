from django import template 

# register=template.from django import template

register = template.Library()


def custom_filter(value):
    return value[0:100]+"..."

register.filter("custom_filter",custom_filter) 