from datetime import timedelta, time, datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from clinic.models import Clinic

def index(req):
    clinics = Clinic.objects.all()

    2h = timedelta(hours=2)

    for cl in clinics:
        datetime(cl.last_update)
        dt = timedelta(minutes=cl.est_wait_min)

        datetime.now()

        cl.waiting = 40



    ctx = { 'clinics': clinics,
    }


    return render(req, 'clinic/hello.html', ctx)


