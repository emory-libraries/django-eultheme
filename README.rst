django-eultheme
===============

Reusable Emory University Libraries theme/templates for use with Django applications


Use and Installation:
---------------------

* pip install via github url
* Add ``eultheme`` to installed apps
* Extend ``eultheme/site_base.html`` for your base template.
* Recommended: add ``eultheme.context_processors.template_settings`` to
  your **TEMPLATE_CONTEXT_PROCESSORS**

Expects that you are using :mod:`django.contrib.staticfiles`, and that
**TEMPLATE_LOADERS** and **STATICFILES_FINDERS** are configured to load
files from app directories (included in the default settings).

Recommended: setup a context processor to include your project version
in all templates as **SW_VERSION**.

Include **eultheme.js** in your site base if you use any of the template snippets
that require it (e.g., advanced search filters).

**NOTE**: We use git flow naming conventions for this git repository.
New development will always be in in *develop* and the most recent
release, once there is one, will be in *master*.
