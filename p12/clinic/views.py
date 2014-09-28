from datetime import timedelta, time, datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from clinic.models import Clinic

def index(req):
    clinics = Clinic.objects.all()

    hours2 = timedelta(hours=2)

    for cl in clinics:
        cl.last_update
        dt = timedelta(minutes=cl.est_wait_min)

        now = datetime.now()
        now = now.replace(tzinfo=None)
        lu = cl.last_update
        lu = lu.replace(tzinfo=None)
        if now - (lu + dt) > hours2:
            cl.waiting = 'unknown'
        else:
            cl.waiting = int(dt.seconds) / 60


    ctx = { 'clinics': clinics,
    }


    return render(req, 'clinic/hello.html', ctx)


