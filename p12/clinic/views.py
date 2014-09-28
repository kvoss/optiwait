from django.shortcuts import render
from django.http import HttpResponse

from clinic.models import Clinic

def index(req):
    ctx = { 'clinics': Clinic.objects.all() }
    return render(req, 'clinic/hello.html', ctx)


