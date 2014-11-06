#import json
import re
import twitter

from clinic.parser import Parser
from dateutil.parser import parse

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values   
# for these credentials, which you'll need to provide in place of these           
# empty string values that are defined as placeholders.                           
# See https://dev.twitter.com/docs/auth/oauth for more information                
# on Twitter's OAuth implementation.                                              

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
    #for msg in tts:
    #    print json.dumps(msg['text'], indent=2)
    msg = tts[0]
    dt = parse(msg['created_at'])

    ret = (dt, msg['text'])
    return ret


def get_update(tt_id):
    DEFAULT_WAIT = 60

    try:
        t, txt = get_msgs(tt_id)
    except IndexError:
        raise TweetError
    except Exception, e: #XXX: catch other exceptions and report
        print '[!]>> EXCEPTION: ', e
        raise TweetError

    mins = Parser(txt).get_minutes()

    return (t, mins)

#print get_update('LMCSaskatoon')

