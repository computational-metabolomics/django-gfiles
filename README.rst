=====
gfiles
=====

Simple file management of generic files.

Detailed documentation is in the "docs" directory (todo)

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
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('gfiles/', include('gfiles.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add files. Or add as user http://127.0.0.1:8000/upload_gfile/ and
    view files as user http://127.0.0.1:8000/gfile_summary/
