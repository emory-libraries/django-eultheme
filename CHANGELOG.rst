CHANGELOG
=========


Release 0.5
-----------

- Added block for metadata
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
