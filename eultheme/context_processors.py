import datetime
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject
from django.utils.timezone import utc
from downtime.models import Period
from .models import Banner


def template_settings(request):
    '''Template context processor: add selected setting to context
    so it can be used on any page .'''

    context_extras = {
        'ENABLE_BETA_WARNING': getattr(settings, 'ENABLE_BETA_WARNING', False),
        'EULTHEME_NO_EXTERNAL_JS': getattr(settings, 'EULTHEME_NO_EXTERNAL_JS', False)}

    return context_extras


def site_path(request):
    '''Template context processor: provides access to current
    :class:`~django.contrib.sites.models.Site` and
    the site root path for use in building absolute urls.
    '''
    site = SimpleLazyObject(lambda: get_current_site(request))
    protocol = 'https' if request.is_secure() else 'http'
    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "%s://%s" % (protocol, site.domain))}


def downtime_context(request):
    '''Template context processor: add relevant maintenance banner to site.'''
    banner = Banner.objects.get_deployed().first()
    context = {}
    if banner:
        context.update({'banner': banner})

    site_is_down = Period.objects.is_down()
    if site_is_down:
        context.update({'site_is_down': site_is_down})
    return context
