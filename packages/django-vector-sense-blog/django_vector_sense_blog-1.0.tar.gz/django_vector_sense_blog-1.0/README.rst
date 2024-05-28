==========================
Django Vector Sense App
==========================

Geocoder app

Quick Start
===========

1. Add "django_blog" to your ``INSTALLED_APPS`` settings like this::

    INSTALLED_APPS = [
        ...
        'django_blog',
    ]

2. Include the polls URLconf in your project ``urls.py`` like this::

    path('django_blog/', include('django_blog.urls', namespace='django_blog')),

3. Run ``python manage.py migrate`` to create the Blogs models.

4. Start the development server and visit ``http://localhost:8080`` to run the app.
