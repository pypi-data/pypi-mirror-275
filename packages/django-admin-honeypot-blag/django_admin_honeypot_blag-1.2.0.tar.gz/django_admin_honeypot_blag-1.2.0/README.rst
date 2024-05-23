=====================
django-admin-honeypot
=====================

.. image:: https://img.shields.io/pypi/v/django-admin-honeypot-blag.svg
   :target: https://pypi.python.org/pypi/django-admin-honeypot-blag/
   :alt: pypi version

.. image:: https://pepy.tech/badge/django-admin-honeypot-blag/
   :target: https://pepy.tech/project/django-admin-honeypot-blag/
   :alt: pypi downloads


**django-admin-honeypot** is a fake Django admin login screen to log and notify
admins of attempted unauthorized access. This app was inspired by discussion
in and around Paul McMillan's security talk at DjangoCon 2011.

* **Original Author**: `Derek Payton <http://dmpayton.com/>`_
* **Version**: 1.2.0
* **License**: MIT

Documentation
=============

http://django-admin-honeypot.readthedocs.io

tl;dr
-----

* Install django-admin-honeypot-blag from PyPI::

        pip install django-admin-honeypot-blag

* Add ``admin_honeypot`` to ``INSTALLED_APPS``
* Update your urls.py:

    ::

        urlpatterns = [
            ...
            path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
            path('secret/', admin.site.urls),
        ]

* Run ``python manage.py migrate``

NOTE: replace ``secret`` in the url above with your own secret url prefix
