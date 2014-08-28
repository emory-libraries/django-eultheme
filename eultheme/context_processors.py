from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.utils.functional import SimpleLazyObject

def template_settings(request):
    '''Template context processor: add selected setting to context
    so it can be used on any page .'''

    context_extras = {
        'ENABLE_BETA_WARNING': getattr(settings, 'ENABLE_BETA_WARNING', False),
        'EULTHEME_NO_EXTERNAL_JS': getattr(settings, 'EULTHEME_NO_EXTERNAL_JS', False),
    }

    return context_extras

def site_path(request):
	'''Template context processor: defines current site and 
	the site root path so it can be used when building absolute urls.'''
    site = SimpleLazyObject(lambda: get_current_site(request))
    protocol = 'https' if request.is_secure() else 'http'

    return {
        'site': site,
        'site_root': SimpleLazyObject(lambda: "{0}://{1}".format(protocol, site.domain)),
    }