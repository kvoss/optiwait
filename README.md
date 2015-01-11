# django-clinic

Clinic is a Django app that provides:

## Quick start

1. Add "clinic" to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'clinic',
    )

2. Include the clinic URLconf in your project `urls.py`:

    url(r'^clinic/', include('clinic.urls')),

3. Run `python manage.py migrate` to create the clinic models.

4. Start the development server and visit `http://127.0.0.1:8000/clinic`.

5. Visit `http://127.0.0.1:8000/clinic/stats` to display stats.

