django-eultheme
===============

Reusable Emory University Libraries theme/templates for use with Django applications

.. image:: https://travis-ci.org/emory-libraries/django-eultheme.svg?branch=feature%2Fmaintenance_notifications
    :target: https://travis-ci.org/emory-libraries/django-eultheme

Use and Installation:
---------------------


* pip install via github url::

     pip install -e git://github.com/emory-libraries/django-eultheme.git#egg=eultheme

* Update **INSTALLED_APPS** to include the following::

    'django.contrib.humanize',
    'eultheme',
    'widget_tweaks',
    'downtime'


* Extend ``eultheme/site_base.html`` for your base template.
* *Recommended:* update **TEMPLATE_CONTEXT_PROCESSORS** to include::

    eultheme.context_processors.template_settings

* *Recommended:* create a context processor to include your project version
  in all templates as **SW_VERSION**.  If it is set, eultheme will display
  the current version in the footer.  Example version context processor::

      from myproject import __version__

      def version(request):
          return {'SW_VERSION': __version__}

* Include **eultheme.js** in your site base (or other templates as appropriate)
  if you use any of the template snippets that require it
  (e.g., advanced search filters).


**eultheme** expects that you are using ``django.contrib.staticfiles``, and that
**TEMPLATE_LOADERS** and **STATICFILES_FINDERS** are configured to load
files from app directories (included in the default settings).  It also
expects a named url called ``site-index``.


Downtime/Maintenance pages
--------------------------

eultheme includes maintenance functionality based on `django-downtime`_.

.. _django-downtime: https://github.com/dstegelman/django-downtime

To enable downtime functionality and maintenance banners before
scheduled downtimes, add the following configurations.

* Update **MIDDLEWARE_CLASSES** to include::

    eultheme.middleware.DownpageMiddleware

  This should be included after
  ``django.contrib.auth.middleware.AuthenticationMiddleware`` and
  ``django.contrib.sessions.middleware.SessionMiddleware``.

* Update **TEMPLATE_CONTEXT_PROCESSORS** to include::

    eultheme.context_processors.downtime_context

* Add downtime exempt paths to your local settings for URLs that
  are not affected by the downtime. This will allow access to parts of
  the site even if when the site is down for scheduled maintenance::

      # exempted paths for downtime
      DOWNTIME_EXEMPT_PATHS = (
          '/admin',
      )

* Add downtime exempt IP addresses to your local settings.  This will
  allow access to the entire site even when the site is scheduled to
  be down hen accessing it with one of the listed IPs.::

     # list of IPs that can access the site despite downtime
     DOWNTIME_ALLOWED_IPS = ['127.0.0.1']

You can customize downtime pages by adding a ``downtime/downtime.html``
template that extends ``eultheme/downtime_base.html``.

If you are not extending ``eultheme/site_base.html`` for your base
template, you can include maintenance banners by including the
``mx/banner.html`` snippet.


----

**NOTE**: We use git flow naming conventions for this git repository.
New development will always be in in *develop* and the most recent
release, once there is one, will be in *master*.
