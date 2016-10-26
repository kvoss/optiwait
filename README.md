# optiwait

optiwait provides estimated waiting times for walk-in clinics.
The estimated waiting time is based on wait time provided by clinics via twitter,
and on the distance to available clinics.
The web interface and data model are based on Django.

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
