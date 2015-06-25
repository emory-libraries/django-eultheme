django-eultheme
===============

Reusable Emory University Libraries theme/templates for use with Django applications

.. image:: https://travis-ci.org/emory-libraries/django-eultheme.svg?branch=feature%2Fmaintenance_notifications
    :target: https://travis-ci.org/emory-libraries/django-eultheme

Use and Installation:
---------------------

* pip install via github url
* Add ``eultheme``, ``widget_tweaks``, and ``downtime`` to **INSTALLED_APPS**
* Add ``eultheme.middleware.DownpageMiddleware`` to **MIDDLEWARE_CLASSES** after ``django.contrib.sessions.middleware.SessionMiddleware`` and ``django.contrib.auth.middleware.AuthenticationMiddleware``
* Extend ``eultheme/site_base.html`` for your base template.
* Recommended: add ``eultheme.context_processors.template_settings`` to
  your **TEMPLATE_CONTEXT_PROCESSORS**

Expects that you are using :mod:`django.contrib.staticfiles`, and that
**TEMPLATE_LOADERS** and **STATICFILES_FINDERS** are configured to load
files from app directories (included in the default settings).

Recommended: add downtime exempt paths to your local settings.
This will allow access to parts of the site even if the site marked as down.
::

  # exempted paths for downtime
  DOWNTIME_EXEMPT_PATHS = (
      '/admin',
  )

Recommended: add downtime exempt IP addresses to your local settings.
This will allow access to the entire site even if the site is marked as be down
when accessing it with one of the listed IPs.
::

  # list of IPs that can access the site despite downtime
  DOWNTIME_ALLOWED_IPS = ['127.0.0.1']


Recommended: setup a context processor to include your project version
in all templates as **SW_VERSION**.

Include **eultheme.js** in your site base if you use any of the template snippets
that require it (e.g., advanced search filters).

**NOTE**: We use git flow naming conventions for this git repository.
New development will always be in in *develop* and the most recent
release, once there is one, will be in *master*.
