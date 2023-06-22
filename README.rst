=====
django-gfiles
=====

Simple file management of generic files.

Further documentation available on `ReadTheDocs <https://mogi.readthedocs.io/en/latest/>`__




Quick start
-----------

1. Add "gfiles" and django application dependencies to your INSTALLED_APPS in the settings file::

    INSTALLED_APPS = [
        ...
        'gfiles',

        'django_tables2',
        'bootstrap3',
        'django_tables2_column_shifter',
        'django_sb_admin',
        'django_filters',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
    ]

2. Add custom auth and login in settings file:

    AUTH_USER_MODEL = 'gfiles.User'
    LOGIN_REDIRECT_URL = 'index'
    LOGIN_URL = '/accounts/login/'

3. Include the polls URLconf in your project urls.py like this::

    url('gfiles/', include('gfiles.urls')),

4. Run `python manage.py migrate` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000

6. Register http://127.0.0.1:8000/accounts/signup/ and login http://127.0.0.1:8000/accounts/login/

7. Add files (need to be logged in) http://127.0.0.1:8000/upload_gfile/

8. View and filter files http://127.0.0.1:8000/gfile_summary/