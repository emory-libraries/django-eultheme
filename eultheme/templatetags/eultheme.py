from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def messagetag_css(value):
    '''convert django message tags to equivalent Bootstrap CSS class'''
    if value in ['success', 'info', 'warning']:
        return 'bg-%s' % value
    elif value == 'error':
        return 'bg-danger'
    elif value == 'debug':
        return 'bg-primary' #?
