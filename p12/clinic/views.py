from datetime import timedelta, time, datetime

from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone

from clinic.models import Clinic

import twitter
from dateutil.parser import parse

class TweetError(Exception):
    pass

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


def get_time(tt_id):
    if tt_id == '':
        raise TweetError
    else:
        ret = get_msgs(tt_id)
    return ret['update']

def index(req):
    clinics = Clinic.objects.all()

    hours2 = timedelta(hours=2)

    for cl in clinics:
        # updating the DB
        try:
            t = get_time(cl.twitter)
            print '[!]>> ', cl.name, t
            print '[!]>> ', cl.name, cl.last_update
            if t > cl.last_update:
                cl.last_update = t
                cl.save()
        except TweetError:
            pass

        dt = timedelta(minutes=cl.est_wait_min)

        now = datetime.now()
        now = now.replace(tzinfo=None)
        # last update
        lu = cl.last_update
        lu = lu.replace(tzinfo=None)


        if now - (lu + dt) > hours2:
            cl.waiting = 'unknown'
        else:
            cl.waiting = int(dt.seconds) / 60


    ctx = { 'clinics': clinics,
    }


    return render(req, 'clinic/hello.html', ctx)


