from datetime import timedelta, time, datetime
from dateutil.parser import parse
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse

from clinic.models import Clinic

import twitter

import re

class TweetError(Exception):
    pass

PATTERN = re.compile(r'(\d+) [Mm]in')
PATTERNH = re.compile(r'(\d+) [Hh]our')

CONSUMER_KEY = 'lMk5wnSsEqRFqB6wTyQ00TlLk'
CONSUMER_SECRET ='A0XRy7zkgFej4fnTNqbKLF4QOhIRU6ygIul00JVYGE84BpPsO5'
OAUTH_TOKEN = '2835226370-1kIFZSqIsw9obeEFPGlkFhj3vwpSLna4aVcrCYK'
OAUTH_TOKEN_SECRET = 'NfAQTO3S2bQV4t95L6u3L71oZmtbhzjcfT9BXbgsjQ1fZ'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

def get_msgs(clinic_id):
    tts =  twitter_api.statuses.user_timeline(screen_name=clinic_id)
    msg = tts[0]
    dt = parse(msg['created_at'])

    ret = {'update' : dt, 'msg': msg['text'] }

    return ret


def get_update(tt_id):
    if tt_id == '':
        raise TweetError
    else:
        ret = get_msgs(tt_id)
    return (ret['update'], ret['msg'])


HOUR = timedelta(hours=1)

def index(req):
    clinics = Clinic.objects.all()

    for cl in clinics:
        try:
            t, txt = get_update(cl.twitter)

            sre = PATTERN.search(txt)
            sreh = PATTERNH.search(txt)
            #print txt
            if sre:
                mins = sre.groups(1)
                mins = int( mins[0])
            elif sreh:
                hours = sreh.groups(1)
                mins = int(hours[0]) * 60
            else:
                mins = 60

            print '[!]>> ', cl.name, t
            print '[!]>> ', cl.name, cl.last_update

            if t >= cl.last_update:
                # updating the DB
                cl.last_update = t
                cl.est_wait_min = mins
                cl.save()
        except TweetError:
            pass

        dt = timedelta(minutes=cl.est_wait_min)
        lu = cl.last_update

        now = timezone.now()

        # if no update in the past 8 hours
        #  assumes a clinic works 8 hours and posted update first time in the
        #  morning.
        # XXX: this perios should be shortened but I dont like seeing 'unknown'
        if (now - (lu + dt)) > (8 * HOUR):
            cl.waiting = 'unknown'
        else:
            cl.waiting = int(dt.seconds) / 60

    ctx = { 'clinics': sorted(clinics, key=lambda x: x.waiting),
    }

    return render(req, 'clinic/hello.html', ctx)

