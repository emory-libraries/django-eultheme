CHANGELOG
=========

Release 1.4.1
-------------
Changed the import for `get_current_site` for Django 1.9 compatibility. See http://djbook.ru/rel1.9/releases/1.7.html#moved-objects-in-contrib-sites

Release 1.3
-----------

- Update context processors for django 1.9+ compatibility
- Drop python 2.6 and django 1.5 from travis-ci test matrix

Release 1.3
-----------

- Update **django.contrib.messages** for newer versions of Django
  and to handle messages with multiple tags.
- Admin link in site base navigation now includes a FontAwesome icon
  and span to customize display, e.g. for smaller screens
- Body placement now uses margin instead of padding for fixed header layout

Release 1.2.1
-------------

- Update to Bootstrap v3.3.6.

Release 1.2
-----------

- Update pagination snippets **pagination_all_pages** and **pagination_dropdown**
  to use standard pagination context objects provided by Django's class-based views.

.. Warning::

    Pagination template context variable changes are *not* backwards
    compatible.


Release 1.1.2
-------------

- Added south migrations for older versions of Django (<1.7)

Release 1.1.1
-------------

- Wording improvements for downtime banner and page, for clarity and
  to handle all variant cases.

Release 1.1
-----------

- Banners show time range (i.e. noon to 6pm) for downtimes less than 24 hours.
- Simplified downtime message to show end time.

Release 1.0
-----------

- Added dependency **django-downtime**
- Added maintenance banners to display downtime warnings
- New context processor, **downtime_context**, to add relevant
  maintenance information to site
- New management command, `disable_downtime`, to disable all downtime periods
- Added base downtime template `eultheme/downtime_base.html` that extends `eultheme/site_base.html`
- New block for maintenance banner, **mx_banner**
- New html template for downtime pages based on Bootstrap
- New snippet for maintenance banners

Release 0.5
-----------

- Added new template block for header metadata, e.g. Twitter or OpenGraph integration
- New icons from Font Awesome (http://fortawesome.github.io/Font-Awesome/icons/)
- New dropdown pagination template
- New context processor, **site_path**, for access to the current configured
  site via django.contrib.sites

Release 0.4
-----------

- Improved Emory branding in header and footer
- New block for mobile nav title, **xs-nav-title**
- Improved style for version number in template footer
- Body attributes block, **body_attrs**, to allow setting RDFa schema.org classes

Release 0.3
-----------

- Updated Emory branding
- Optional beta warning banner, configurable via **ENABLE_BETA_WARNING**
  in Django settings

Release 0.2
-----------

- Added **head_extras** block to site_base.html to allow for additional
  head items (e.g., metadata, unAPI server links, etc)
- New Django setting **EULTHEME_NO_EXTERNAL_JS** - configure this to be true
  when you need Javascript resources to be loaded from local static files
  instead of a public CDN

Release 0.1
-----------

Reusable django theme based on Twitter Bootstrap
- site base template to be extended
- template snippet and CSS for card-style search result
- template snippet and CSS for advanced search filters
- template snippet and CSS for pagination
- CSS and sample templates for 404, 403, and 500 error pages
