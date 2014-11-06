from datetime import timedelta
from django.utils import timezone

from django.shortcuts import render
#from django.http import HttpResponse
from django import forms

from clinic.models import Clinic
from clinic.distance import get_distances

HOUR = timedelta(hours=1)

#class LocationForm(forms.Form):
#    location = forms.CharField(max_length=70) 
#    #, attrs={'placeholder': 'Type in your city'})

def index(req):

    # XXX: this should be read from the req
    LOCATION = '701 5th Ave N, Saskatoon'
    if req.method == 'POST':
        if 'location' in req.POST:
            LOCATION = req.POST['location']

    now = timezone.now()

    #clinics = Clinic.get_allvalid()
    clinics = Clinic.objects.filter(valid=True).all()
    for cl in clinics:
        cl.refresh()
        dt = timedelta(minutes=cl.est_wait_min)
        lu = cl.last_update

        # if no update in the past 8 hours from last update time
        #  assumes a clinic works 8 hours and posted update first time in the
        #  morning.
        # XXX: this perios should be shortened but I dont like seeing 'unknown'
        if (now - (lu + dt)) > (8 * HOUR):
            cl.waiting = 'unknown'
        else:
            cl.waiting = int(dt.seconds) / 60

    #  Add information about distances
    clocations = map(lambda c: c.location, clinics)
    dstns = get_distances(LOCATION, clocations)
    for c, (l, d) in zip(clinics, dstns):
        if c.location == l: c.distance = d

    # Fill placeholders in the template 
    ctx = {'clinics': sorted(clinics, key=lambda x: x.waiting), 
           #'form' : LocationForm(), 
    }
    return render(req, 'clinic/hello.html', ctx)

