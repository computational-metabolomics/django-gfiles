=====
django-gfiles
=====

|Build Status (Travis)| |Py versions|


Simple file management of generic files.

Further documentation available on `ReadTheDocs <https://mogi.readthedocs.io/en/latest/>`__




Quick start
-----------

1. Add "gfiles" and django application dependencies to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gfiles',

        'django_tables2',
        'bootstrap3',
        'django_tables2_column_shifter',
        'django_sb_admin',
        'django_filter'
    ]

2. Include the polls URLconf in your project urls.py like this::

    url('gfiles/', include('gfiles.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000

5. Register http://127.0.0.1:8000/register/ and login http://127.0.0.1:8000/login/

6. Add files (need to be logged in) http://127.0.0.1:8000/upload_gfile/

7. View and filter files http://127.0.0.1:8000/gfile_summary/



.. |Build Status (Travis)| image:: https://travis-ci.com/computational-metabolomics/django-gfiles.svg?branch=master
   :target: https://travis-ci.com/computational-metabolomics/django-gfiles/

.. |Py versions| image:: https://img.shields.io/pypi/pyversions/django-gfiles.svg?style=flat&maxAge=3600
   :target: https://pypi.python.org/pypi/django-gfiles/
