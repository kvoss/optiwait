from datetime import timedelta, time, datetime
from django.utils import timezone

from django.shortcuts import render
#from django.http import HttpResponse
from django import forms

from clinic.models import Clinic
from clinic.tweets import get_update, TweetError
from clinic.distance import get_distances

HOUR = timedelta(hours=1)

class LocationForm(forms.Form):
    location = forms.CharField(max_length=70) #, attrs={'placeholder': 'Type in your city'})

def index(req):

    # XXX: this should be read from the req
    LOCATION = '701 5th Ave N, Saskatoon'
    if req.method == 'POST' and 'location' in req.POST and req.POST['location']:
        LOCATION = req.POST['location']

    now = timezone.now()

    clinics = Clinic.objects.all()
    for cl in clinics:
        dt = timedelta(minutes=cl.est_wait_min)
        lu = cl.last_update

        try:
            t, mins = get_update(cl.twitter)

            print '[!]>> ', cl.name, cl.last_update, t

            if t > lu:
                # updating the DB
                cl.last_update = t
                cl.est_wait_min = mins
                cl.save()
                lu = cl.last_update
        except TweetError:
            pass

        # if no update in the past 8 hours
        #  assumes a clinic works 8 hours and posted update first time in the
        #  morning.
        # XXX: this perios should be shortened but I dont like seeing 'unknown'
        if (now - (lu + dt)) > (8 * HOUR):
            cl.waiting = 'unknown'
        else:
            cl.waiting = int(dt.seconds) / 60

    clocations = map(lambda c: c.location, clinics)
    dstns = get_distances(LOCATION, clocations)
    for c, d in zip(clinics, dstns):
        c.distance = d[1]

    ctx = { 
            'clinics': sorted(clinics, key=lambda x: x.waiting), 
            #'form' : LocationForm(),
    }

    return render(req, 'clinic/hello.html', ctx)

