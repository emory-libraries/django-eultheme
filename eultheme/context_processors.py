from django.conf import settings


def template_settings(request):
    '''Template context processor: add selected setting to context
    so it can be used on any page .'''

    context_extras = {
        'ENABLE_BETA_WARNING': getattr(settings, 'ENABLE_BETA_WARNING', False),
        'EULTHEME_NO_EXTERNAL_JS': getattr(settings, 'EULTHEME_NO_EXTERNAL_JS', False),
    }

    return context_extras