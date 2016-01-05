from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def messagetag_css(value):
    '''convert django message tags to equivalent Bootstrap CSS class'''
    # value could be multiple, space-separated tags
    tags = value.split(' ')
    for level in ['success', 'info', 'warning']:
        if level in tags:
            return 'bg-%s' % level
    if 'error' in tags:
        return 'bg-danger'
    elif 'debug' in tags:
        return 'bg-primary'  # ?
